#!/usr/bin/env python3
import os
import subprocess
import tkinter as tk 
from tkinter import ttk
import tkinter.messagebox

#Global variables
interface_name = 'Wi-Fi'
hostname = '104.131.190.99'
ssh_id_file = '~/.ssh/digitalocean.pem'
port = 1080

class Application(ttk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill = 'both', expand = 1, ipadx=50)
        self.mainWindowWidgets()
    def mainWindowWidgets(self):
        self.quitButton = ttk.Button(self, text = 'Quit', command = self.quit)
        self.proxyOnButton = ttk.Button(self, text = 'Proxy On', command = proxy_on)
        self.proxyOffButton = ttk.Button(self, text = 'Proxy Off', command = proxy_off)
        self.proxyOnButton.pack(fill = 'x')
        self.proxyOffButton.pack(fill = 'x')
        self.quitButton.pack(fill = 'x')

def is_proxy_on():
    raw = subprocess.check_output(['networksetup', '-getsocksfirewallproxy', interface_name])
    state = raw.split()[1].decode()
    if state == 'Yes':
        return True
    elif state == 'No':
        return False
    else:
        return 'Error'
    
def proxy_on():
    subprocess.call(['networksetup', '-setsocksfirewallproxystate', interface_name, 'on'])
    
def proxy_off():
    subprocess.call(['networksetup', '-setsocksfirewallproxystate', interface_name, 'off'])
    
def set_SOCKS_port(port):
    subprocess.call(['networksetup', '-setsocksfirewallproxy', interface_name, 'localhost', port, 'off'])

#Initialise the application
app = Application()
#Method calls for window management
app.master.title("Proxy Widget")
app.master.maxsize(400, 400)
#start the application
app.mainloop()


        
        


        
        
