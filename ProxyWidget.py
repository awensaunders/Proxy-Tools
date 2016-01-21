#!/usr/bin/env python3
import platform
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from modules import ssh
from modules import socks
from modules import configurator

#Global variables

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
        
        self.interfaceLabel = ttk.Label(self.optionsFrame, text = 'Interface:')
        self.interfaceEntry = ttk.Entry(self.optionsFrame)
        self.interfaceEntry.insert(0, config['interface'])
        self.interfaceLabel.pack(anchor = "w")
        self.interfaceEntry.pack()
        
        self.portLabel = ttk.Label(self.optionsFrame, text = 'Local Port:')
        self.portNumberEntry = ttk.Entry(self.optionsFrame)
        self.portNumberEntry.insert(0, config['port'])
        self.portLabel.pack(anchor = "w")
        self.portNumberEntry.pack()
        
        self.sshPortLabel = ttk.Label(self.optionsFrame, text = 'SSH Port:')
        self.sshPortEntry = ttk.Entry(self.optionsFrame)
        self.sshPortEntry.insert(0, config['sshport'])
        self.sshPortLabel.pack(anchor = "w")
        self.sshPortEntry.pack()
        
        self.userLabel = ttk.Label(self.optionsFrame, text = 'SSH User:')
        self.userEntry = ttk.Entry(self.optionsFrame)
        self.userEntry.insert(0, config['user'])
        self.userLabel.pack(anchor = "w")
        self.userEntry.pack()
        
        self.idLabel = ttk.Label(self.optionsFrame, text = 'SSH Keyfile:')
        self.chooseIdButton = ttk.Button(self.optionsFrame, text = 'Choose...', command = self.choose_id)
        self.idLabel.pack(anchor = "w")
        self.chooseIdButton.pack(anchor = "w")
        
        self.hostnameLabel = ttk.Label(self.optionsFrame, text = 'Hostname:')
        self.hostnameEntry = ttk.Entry(self.optionsFrame)
        self.hostnameEntry.insert(0, config['hostname'])
        self.hostnameLabel.pack(anchor = "w")
        self.hostnameEntry.pack()
        self.applyFrame = ttk.Frame(self.optionsFrame)
        self.applyFrame.pack(fill = 'x', expand = 1, ipadx = 0, ipady = 0)
        self.applyButton = ttk.Button(self.applyFrame, text = 'Apply', command = self.apply_options)
        self.cancelButton = ttk.Button(self.applyFrame, text = 'Cancel', command = self.cancel)
        self.applyButton.pack(side = 'right')
        self.cancelButton.pack(side = 'right')
    def cancel(self):
        print('Dummy function for cancel.')
    def apply_options(self):
        config['interface'] = self.interfaceEntry.get()
        print('Interface:', config['interface'])
        config['port'] = int(self.portNumberEntry.get())
        print('Local Port:', config['port'])
        config['sshport'] = int(self.sshPortEntry.get())
        print('SSH Port:', config['sshport'])
        config['user'] = self.userEntry.get()
        print('User:', config['user'])
        config['hostname'] = self.hostnameEntry.get()
        print('Hostname:', config['hostname'])
        conf.write_config(config)
    def proxy_on(self):
        pro.proxy_on()
        self.proxyOnButton['state'] = 'disabled'
        self.proxyOffButton['state'] = 'enabled'
        ssh_tunnel.start_tunnel(config['user'], config['hostname'], config['sshport'], config['port'], config['ssh_id'])
    def proxy_off(self):
        ssh_tunnel.stop_tunnel()
        pro.proxy_off()
        self.proxyOffButton['state'] = 'disabled'
        self.proxyOnButton['state'] = 'enabled'
    def choose_id(self):
        print('Dummy function for SSH id choice.')

#Initialise an instance of the configurator class
conf = configurator.ConfigFile('./config.yml')
config = conf.read_config()
#Initialise an instance of the ProxyTools class
pro = socks.ProxyTools(config['interface'])
#Initialise an instance of the ssh tunnel class
ssh_tunnel = ssh.Tunnel()

#start the application if main
if __name__ == '__main__':
    if platform.system() != 'Darwin':
        tk.messagebox.showerror("Error", "Unfortunately your operating system is not supported. If you wish to contribute to the development of a port, visit the github repository for this project.")
    else:
        #Initialise the application
        app = Application()
        app.master.title("Proxy Widget")
        app.master.maxsize(400, 400)
        #start the application
        app.mainloop()