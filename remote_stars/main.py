import numpy as np
import matplotlib.pyplot as plt
import socket




host = "84.237.21.36"
port = 5152


def recval(sokc, n):
    data = bytearray()
    while len(data) < n:
        packet  = sock.recv(n-len(data))
        if not packet:
            return
        data.extend(packet)
    return data

def find_max(B):
    local1 = [0,0]
    local2 = [0,0]
    
    for y in range (1, B.shape[0]-1):
        for x in range (1, B.shape[1]-1):

            if B[x,y]>B[x+1,y] and B[x,y]>B[x,y+1]  and B[x,y]>B[x-1,y] and B[x,y]>B[x,y-1]:
                if local1[0]==0 and local1[1]==0:
                    local1[0]=y
                    local1[1]=x
                else:
                    local2[0]=y
                    local2[1]=x
    
    return local1, local2 

def lens(local1, local2):
    len1 = local1[0] - local2[0]
    len2 = local1[1] - local2[1]

    return round(len1**len1 + len2**len2, 1)




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    beat = 'nope'
    while beat != b'yep':
        sock.send(b"get")
        bts = recval(sock, 40002)
                

        im1 =  np.frombuffer(bts[2:40002], dtype="uint8").reshape(bts[0],bts[1])
        

        
        
        local1, local2 = find_max(im1)
        res = lens(local1, local2)


        sock.send(f"{res}".encode())
        print(sock.recv(20))

        sock.send(b"beat")
        beat = sock.recv(20)
        print(beat)

    # plt.subplot(121)
    # plt.title(f"{post1}")
    # plt.imshow(im1)
    # plt.subplot(122)
    # plt.title(f"{post2}")
    # plt.imshow(im1)
    # plt.show()