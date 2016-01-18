#!/usr/bin/env python3
import pytest
import subprocess
import sys
from modules import ssh 
from modules import socks
import ProxyWidget

class TestSOCKS: 
    @pytest.fixture
    def SOCKS_setup(self):
        return socks.ProxyTools('Wi-Fi')
        
    def test_SOCKS_exists(self, SOCKS_setup):
        assert hasattr(SOCKS_setup, 'is_proxy_on')
        
    def test_SOCKS_is_proxy_on(self, SOCKS_setup):
        pass
        #not implemented 
        
class TestSSH:
    @pytest.fixture
    def ssh_setup(self):
        return ssh.Tunnel()
        
    def test_ssh_exists(self):
        assert subprocess.call(['ssh'], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) == 255
    
    def test_ssh_arguments(self, ssh_setup):
        with pytest.raises(TypeError):
            ssh_setup.start_tunnel("asdfljkl")
        
class TestYAML:
    #Not done yet
    pass
