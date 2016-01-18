#!/usr/bin/env python3
import platform
import tkinter as tk 
from tkinter import ttk
import tkinter.messagebox
from modules import ssh 
from modules import socks

#Global variables
interface_name = 'Wi-Fi'
hostname = '104.131.190.99'
ssh_id_file = '/Users/awensaunders/.ssh/digitalocean.pem'
sshport = 22
port = 1080
user = 'root'

#Main app logic
class Application(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack(fill = 'both', expand = 1, ipadx = 1, ipady = 1)
        self.mainWindowWidgets()
    def mainWindowWidgets(self):
        self.quitButton = ttk.Button(self, text = 'Quit', command = self.quit, width = 8)
        self.proxyOnButton = ttk.Button(self, text = 'Proxy On', command = self.proxy_on, width = 8)
        self.proxyOffButton = ttk.Button(self, text = 'Proxy Off', command = self.proxy_off, width = 8)
        self.optionsButton = ttk.Button(self, text = 'Options', command = self.spawnOptionsWindow, width = 8)
        self.proxyOnButton.pack()
        self.proxyOffButton.pack()
        self.optionsButton.pack()
        self.quitButton.pack()
        if pro.is_proxy_on() == True:
            self.proxyOnButton['state'] = 'disabled'
            self.proxyOffButton['state'] = 'enabled'
        elif pro.is_proxy_on() == False:
            self.proxyOnButton['state'] = 'enabled'
            self.proxyOffButton['state'] = 'disabled'
        else:
            tk.messagebox.showerror("Error", "The current state of the proxy could not be determined. ")
   
    def spawnOptionsWindow(self):
        self.optionsWindow = tk.Toplevel(self.master)
        self.optionsFrame = ttk.Frame(self.optionsWindow)
        self.optionsFrame.pack(fill = 'both', expand = 1, ipadx = 1, ipady = 1)
        self.portLabel = ttk.Label(self.optionsFrame, text = 'Port Number:')
        self.portNumberEntry = ttk.Entry(self.optionsFrame)
        self.portNumberEntry.insert(0, port)
        self.portLabel.pack(anchor = "w")
        self.portNumberEntry.pack()
        
        self.hostLabel = ttk.Label(self.optionsFrame, text = 'Hostname:')
        self.hostnameEntry = ttk.Entry(self.optionsFrame)
        self.hostnameEntry.insert(0, hostname)
        self.hostLabel.pack(anchor = "w")
        self.hostnameEntry.pack()
        
        self.applyButton = ttk.Button(self.optionsFrame, text = 'Apply', command = self.apply_options, width = 4)
        self.applyButton.pack()
    def apply_options(self):
        port = int(self.portNumberEntry.get())
        print('Port Number:', port)
        hostname = self.hostnameEntry.get()
        print('Hostname:', hostname)
    def proxy_on(self):
        pro.proxy_on()
        self.proxyOnButton['state'] = 'disabled'
        self.proxyOffButton['state'] = 'enabled'
        ssh_tunnel.start_tunnel(user, hostname, sshport, port, ssh_id_file)
    def proxy_off(self):
        ssh_tunnel.stop_tunnel()
        pro.proxy_off()
        self.proxyOffButton['state'] = 'disabled'
        self.proxyOnButton['state'] = 'enabled'
        
        

#Initialise an instance of the ProxyTools class
pro = socks.ProxyTools(interface_name)
#Initialise an instance of the ssh tunnel class
ssh_tunnel = ssh.Tunnel()
#start the application if main
if __name__ == '__main__':
    if platform.system() != 'Darwin':
        tk.messagebox.showerror("Error", "Unfortunately your operating system is not supported. If you wish to contribute to the development of a port, visit the github repository for this project.")
    else:
        #Initialise the application
        app = Application()

        #Method calls for window management
        app.master.title("Proxy Widget")
        app.master.maxsize(400, 400)
        #start the application
        app.mainloop()