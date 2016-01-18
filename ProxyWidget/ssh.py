#!/usr/bin/env python3
import subprocess
class Tunnel(object):
    def __init__(self):  
        pass  
    def start_tunnel(self, user, host, port, proxyport, identity_path):
        '''Starts an ssh tunnel. Takes 5 arguments: user, host, ssh port, proxy port, identitypath'''
        self.port = str(port)
        self.user = user
        self.proxyport = str(proxyport)
        self.host = host
        self.identity_path = identity_path
        self.proc = subprocess.Popen(['ssh', '-D', self.proxyport, '-l', self.user, self.host, '-p', self.port, '-N', '-i', self.identity_path])
    def stop_tunnel(self):
            return_code = subprocess.call(['killall', 'ssh'])
            print('Killall returned code: ' + str(return_code))