#!/usr/bin/env python3
import pytest
import subprocess
import sys
from modules import ssh 
from modules import socks
from modules import configurator
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
    
    def test_out_equals_in(self, tmpdir):
        f = str(tmpdir.join('config.yml'))
        c = configurator.ConfigFile(f)
        c.write_config({'name': 'Silenthand Olleander', 'race': 'Human'})
        print(c.read_config())
        assert c.read_config() == {'name': 'Silenthand Olleander', 'race': 'Human'}
    def test_append_works(self, tmpdir):
        f = str(tmpdir.join('config.yml'))
        c = configurator.ConfigFile(f)
        c.write_config({'name': 'Silenthand Olleander', 'race': 'Human'})
        c.append_config({'color': 'blue'})
        assert c.read_config() == {'name': 'Silenthand Olleander', 'race': 'Human', 'color': 'blue'} , "append_config failed to write the file"
        c.write_config({'name': 'Silenthand Olleander', 'race': 'Human'})
        assert c.read_config() == {'name': 'Silenthand Olleander', 'race': 'Human'} , "write_config failed to overwrite the appended file"
    