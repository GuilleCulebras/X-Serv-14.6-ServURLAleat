#!/usr/bin/python3

import socket


class webApp:


    def parse(self, request):

        return None

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

    def __init__(self, hostname, port):

        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        mySocket.listen(5)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048)
            print(request.decode('utf-8'))
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()




class urlaleat(webApp): #Unicamente tenemos que añadir lo que sea diferente, si es igual lo hereda de la clase madre
    def process(self, parsedRequest):
        import random
        
        numRand = str(random.randrange(999999999))
        newUrl = "http://localhost:1234/" + numRand

        return("200 OK", "<html><body><h1><a href=" + newUrl + ">Dame otra.</a>")


if __name__ == "__main__": #instanciar
    testUrlAleat = urlaleat("localhost", 1234)