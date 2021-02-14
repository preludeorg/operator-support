import os
import requests
import shutil
from pathlib import Path


class Installer:

    def __init__(self):
        self.host = 'https://download.prelude.org/latest?platform=linux&variant=deb'

    def download(self):
        r = requests.get(self.host)
        with open('operator.deb', 'wb') as f:
            f.write(r.content)

    @staticmethod
    def install():
        os.system('sudo gdebi -n operator.deb')
    
    @staticmethod
    def copy_configs():
        os.makedirs('/home/vagrant/.config', 777)
        os.makedirs('/home/vagrant/.config/Operator/', 777) 
        os.makedirs('/home/vagrant/.config/Operator/workspace', 777)
        os.makedirs('/home/vagrant/.config/Operator/workspace/adversary', 777)  
        if os.path.isfile('/vagrant/configs/settings.yml'):
            shutil.copyfile('/vagrant/configs/settings.yml', '/home/vagrant/.config/Operator/settings.yml')
        if os.path.isfile('/vagrant/configs/schedules.yml'):
            shutil.copyfile('/vagrant/configs/schedules.yml', '/home/vagrant/.config/Operator/schedules.yml')
        for src_file in Path('adversary').glob('*.*'):
            shutil.copyfile(src_file, '/home/vagrant/.config/Operator/workspace/%s' % src_file)


if __name__ == '__main__':
    installer = Installer()
    installer.download()
    installer.install()
    installer.copy_configs()
