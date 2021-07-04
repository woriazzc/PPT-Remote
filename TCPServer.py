from socket import *

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(("", 8899))
    serverSocket.listen(5)
    print("----------1----------")
    clientSocket, clientInfo = serverSocket.accept()  # 此处链接成功后才会输出2
    print("-------2------------")
    recvData = clientSocket.recv(1024)  # 此处收到信息后才会输出3
    print("---------3--------------")
    print("%s:%s" % (str(clientInfo), recvData))

    clientSocket.close()
    serverSocket.close()