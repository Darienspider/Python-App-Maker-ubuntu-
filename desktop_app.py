import os
import getpass


os_user = str(getpass.getuser())



def create_shortcut(file_to_make,file_path):
    
    base_location = '/home/'+os_user+'/Desktop/'+file_to_make+'.desktop'

    key_info = [
        '[Desktop Entry]',
        'Version=1.0',
        'Type=Application',
        'Name='+file_to_make,
        'Comment=App created by'+str(os_user.capitalize),
        'Exec=python3 '+file_path,
        'Icon=',
        'Path=',
        'Terminal=false',
        'StartupNotify=false',]

    with open(base_location,'w') as shortcut:
        for i in key_info:
            shortcut.write("%s\n" % i)