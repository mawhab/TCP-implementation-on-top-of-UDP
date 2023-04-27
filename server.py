import socketserver

class Connection():
    pass

counter = 0

class TCPHeader():
    def __init__(self, header) -> None:
        self.SYN = int(header[0],2)
        self.ACK = int(header[1],2)
        self.FIN = int(header[2],2)
        self.PID = int(header[3:35],2)
        self.seq_num = int(header[35:67],2)
        self.ack_num = int(header[67:99],2)
        self.checksum = int(header[99:227],2)

class MyUDPHandler(socketserver.BaseRequestHandler):
    def split_header_contents(self):
        # APPROACH 1
        
        # res = ''.join(format(i, '08b') for i in self.msg) # convert message to binary
        # header = res[:232] # take first 29 bytes for header
        # content = self.msg[232:] # rest is message
        # content = [content[i:i+8] for i in range(0, len(content), 8)] # split message to bytes
        # self.content = ''.join(chr(int(i,2)) for i in content) # convert message back to string
        
        # APPROACH 2
        
        header = self.msg[:29] # take first 29 bytes for header
        self.content = self.msg[29:] # rest is message
        header = ''.join(format(i, '08b') for i in header) # convert header to binary
        
        self.header = TCPHeader(header)
        
        
    
    def setup(self):
        global counter
        self.counter = counter
        counter +=1
        
    def handle(self):
        self.msg = self.request[0].strip()
        # self.split_header_contents()
        # CHECK WHICH CONNECTION
        # socket = self.request[1]
        # print("{}, {} wrote:".format(self.client_address[0],self.client_address[1]))
        # print('current object counter: {}'.format(self.counter))
        # print(data)
        # socket.sendto(data.upper(), self.client_address)
        
    def send(self):
        pass


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()