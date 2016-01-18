#!/usr/bin/env python3
import subprocess

class ProxyTools(object):
    '''Main class with methods to list/modify mac SOCKS proxy status'''
    def __init__(self, interface):
        self.interface_name = interface
    def is_proxy_on(self):
        '''Determines the current state of the SOCKS proxy. Returns True if the proxy is enabled, and False if it is disabled.'''
        raw = subprocess.check_output(['networksetup', '-getsocksfirewallproxy', self.interface_name])
        state = raw.split()[1].decode()
        if state == 'Yes':
            return True
        elif state == 'No':
            return False
        else:
            return 'Error'
                  
    def proxy_on(self):
        '''Turns the proxy on'''
        subprocess.call(['networksetup', '-setsocksfirewallproxystate', self.interface_name, 'on'])

    def proxy_off(self):
        '''Turns the proxy off'''
        subprocess.call(['networksetup', '-setsocksfirewallproxystate', self.interface_name, 'off'])

    def set_SOCKS_port(self, port):
        '''Configures the socks proxy to localhost:port. Takes one argument: port.'''
        subprocess.call(['networksetup', '-setsocksfirewallproxy', self.interface_name, 'localhost', port, 'off'])