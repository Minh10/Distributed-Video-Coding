import cv2
import socket
import math
import pickle
import sys
import os
import time
max_length = 65000
host = '127.0.0.1'
port = 12008
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
assert len(sys.argv) == 4
sequence = (sys.argv[1])[0:-4]
frameW = int(sys.argv[2])
frameH = int(sys.argv[3])
print(frameW)
print(frameH)
n = 0
cur = time.time()

print(time.time() - cur)
os.system("/home/nanhtrang/AI/x265/build/linux/x265 --input /home/nanhtrang/AI/DVC/code/client/originVideo/" + sequence + ".yuv --fps 30 --input-res " + str(frameW) +"x"+str(frameH)+"  --input-depth 8 --input-csp 1 --ssim --psnr --output /home/nanhtrang/AI/DVC/code/client/originVideo/" + sequence +".bin")
with open("/home/nanhtrang/AI/DVC/code/client/originVideo/" + sequence + ".bin", "rb") as f:
    byte = f.read(650000)
    buffer = byte
    while byte != b"":
        byte = f.read(650000)
        buffer +=byte
buffer_size = len(buffer)
print(buffer_size)
num_of_packs = 1
if buffer_size > max_length:
    num_of_packs = math.ceil(buffer_size/max_length)

frame_info = {"packs":num_of_packs}

# send the number of packs to be expected
sock.sendto(pickle.dumps(frame_info), (host, port))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

left = 0
right = max_length
print(num_of_packs)
recv = b"0"
for i in range(num_of_packs):
    
    # truncate data to send
    data = buffer[left:right]
    #print(data)
    left = right
    right += max_length
    # send the frames accordingly
    recv = b"0"
    while(recv != b"1"):
        recv, address = sock.recvfrom(max_length)
    sock.sendto(data, (host, port))
    
    print(i)
    print(len(data))
print(time.time() - cur)
print("done")
