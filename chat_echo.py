import asyncore
import logging
import socket
import asynchat

class EchoServer(asyncore.dispatcher):
    """Receives connections and establishes handlers for each client.
    """
    
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(5)
        return

    def handle_accept(self):
        # Called when a client connects to our socket
        client_info = self.accept()
        EchoHandler(sock=client_info[0])
        # We only want to deal with one client at a time,
        # so close as soon as we set up the handler.
        # Normally you would not do this and the server
        # would run forever or until it received instructions
        # to stop.
        #self.handle_close()
        return
    
    def handle_close(self):
        self.close()

class EchoHandler(asynchat.async_chat):
    """Handles echoing messages from a single client.
    """

    # Artificially reduce buffer sizes to illustrate
    # sending and receiving partial messages.
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self, sock):
        self.received_data = []
        self.logger = logging.getLogger('EchoHandler')
        asynchat.async_chat.__init__(self, sock)
        # Start looking for the ECHO command
        self.process_data = self._process_command
        self.set_terminator('\n')
        return

    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d bytes)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        """The end of a command or message has been seen."""
        self.logger.debug('found_terminator()')
        self.process_data()
    
    def _process_command(self):        
        """We have the full ECHO command"""
        command = ''.join(self.received_data)
        self.logger.debug('_process_command() "%s"', command)
        command_verb, command_arg = command.strip().split(' ')
        expected_data_len = int(command_arg)
        self.set_terminator(expected_data_len)
        self.process_data = self._process_message
        self.received_data = []
    
    def _process_message(self):
        """We have read the entire message to be sent back to the client"""
        to_echo = ''.join(self.received_data)
        self.logger.debug('_process_message() echoing\n"""%s"""', len(to_echo))
        self.push(to_echo)
        # Disconnect after sending the entire response
        # since we only want to do one thing at a time
        self.close_when_done()

class EchoClient(asynchat.async_chat):
    """Sends messages to the server and receives responses.
    """

    # Artificially reduce buffer sizes to illustrate
    # sending and receiving partial messages.
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64

    myport = None
    
    def __init__(self, host, port, message):
        self.myport = port
        self.message = message
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        return
        
    def handle_connect(self):
        self.logger.debug('handle_connect()')
        # Send the command
        self.push('ECHO %d\n' % len(self.message))
        # Send the data
        self.push_with_producer(EchoProducer(self.message, buffer_size=self.ac_out_buffer_size))
        # We expect the data to come back as-is, 
        # so set a length-based terminator
        self.set_terminator(len(self.message))
    
    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEIVED COPY OF MESSAGE')
            #print self.myport
        else:
            self.logger.debug('ERROR IN TRANSMISSION')
            self.logger.debug('EXPECTED "%s"', len(self.message))
            self.logger.debug('RECEIVED "%s"', len(received_message))
        return

class EchoProducer(asynchat.simple_producer):

    logger = logging.getLogger('EchoProducer')

    def more(self):
        response = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%s bytes)\n"""%s"""', len(response), response)
        return response

if __name__ == '__main__':
  f= '%(name)s: %(message)s'
  logging.basicConfig(level=logging.DEBUG,format=f)

  address = ('localhost', 0) # let the kernel give us a port
  server = EchoServer(address)
  ip, port = server.address # find out what port we were given

  fp = open('PortAsynTest.txt', 'w')
  fp.write(str(port).encode("utf-8"))
  fp.close
  fp = None
  client = EchoClient(ip, port, message="Hallo")

  loop_counter = 0
  while asyncore.socket_map:
      loop_counter += 1
      logging.debug('--->loop_counter=%s', loop_counter)
      asyncore.loop(timeout=1, count=1)



