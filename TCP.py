class TCPHeader():
    def __init__(self, header) -> None:
        self.SYN = int(header[0],2)
        self.ACK = int(header[1],2)
        self.FIN = int(header[2],2)
        self.PID = int(header[3:35],2)
        self.seq_num = int(header[35:67],2)
        self.ack_num = int(header[67:99],2)
        self.checksum = int(header[99:227],2)