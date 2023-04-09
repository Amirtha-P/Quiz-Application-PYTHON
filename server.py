import socket
def server_program():
    # get the hostname
    count=0
    host = '127.0.0.1'
    port = 5000
    print("Host is :",host)
    print("Port which is connected is : ",port);
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket created!!!!")
    s.bind((host, port))
    s.listen(2)
    print("Listening....")
    conn,addr=s.accept()
    print("Accepted.....")
    print("The accepted address is ",addr)
    print(str(addr))
    for i in range(4):
        if(i==0):
            data=conn.recv(1024).decode()
            if(data=="2"):
                count=count+1
        if(i==1):
            data=conn.recv(1024).decode()
            if(data=="1"):
                count=count+1
        if(i==2):
            data=conn.recv(1024).decode()
            if(data=="1"):
                count=count+1
        if(i==3):
            result=str(count)
            conn.send(result.encode())
            print("send successfully")
    print(count)
    conn.close()
server_program()
