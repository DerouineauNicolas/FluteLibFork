import socket
import struct
import zlib

MCAST_GRP = '224.0.23.60'
MCAST_PORT = 4937

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 'vboxnet0')
sock.bind((MCAST_GRP, MCAST_PORT))  # use MCAST_GRP instead of '' to listen only
                             # to MCAST_GRP, not all groups on MCAST_PORT
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
  data=sock.recv(1024)
  print "LLS_table_ID="+data[0]
  LLS_table_ID=ord(data[0])
  print "LLS_group_ID="+data[1]
  print "group_count_minus1="+data[2]
  print "##############################"
  if LLS_table_ID == 1:
    print "SLT Detected"
    #print ord(data[3])
    decompressed_data=zlib.decompress(data[4:],16+zlib.MAX_WBITS)
    print decompressed_data
  elif LLS_table_ID == 2:
     print "RRT Detected"
  elif LLS_table_ID == 3:
     print "System Time Detected"
  elif LLS_table_ID == 4:
     print "AEAT Detected"
  else:
     print "Reserved"
  





  #   print "On screen message notification"
