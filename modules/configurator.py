#!/usr/bin/env python3
import io
import yaml

default = {'exists': True, 'interface': 'Wi-Fi', 'hostname': '104.131.190.99', 'ssh_id': '~/.ssh/id_rsa', 'sshport': 22 ,'port': 1080, 'user': 'root'}

class ConfigFile(object):
    def __init__(self, path):
        """Constructor. Takes 1 argument, filepath"""
        self.path = path
        self.open_file()
    def write_config(self, dict):
        """Writes the config and overwrites any existing data takes one argument"""
        self.file.seek(0)
        self.file.truncate()
        yaml.dump(dict, self.file, default_flow_style=False)
    def append_config(self, dict):
        """Appends the current config, takes one argument"""
        yaml.dump(dict, self.file, default_flow_style=False)
    
    def read_config(self): 
        """Reads the config and returns it as a dictionary"""
        self.file.seek(0)
        return yaml.load(self.file)

    def open_file(self):
        """Opens the config file"""
        try:
            self.file = io.open(self.path, 'r+t')
        
        except IOError:
            try:
                self.file = io.open(self.path, 'a+t')
                print("Config file does not exist -- Creating.")
                self.write_config(default) 
            
            except IOError:
                print("Error! Config file could not be read or written")

def main():
    f = ConfigFile('./config.yml')
    print(f.read_config())
    

if __name__ == '__main__':
    main()
            