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
        if os.path.isfile('settings.yml'):
            shutil.copyfile('settings.yml', '/home/vagrant/.config/Operator/settings.yml')
        if os.path.isfile('schedules.yml'):
            shutil.copyfile('schedules.yml', '/home/vagrant/.config/Operator/settings.yml')
        for src_file in Path('adversary').glob('*.*'):
            shutil.copyfile(src_file, '/home/vagrant/.config/Operator/workspace/%s' % src_file)


if __name__ == '__main__':
    installer = Installer()
    installer.download()
    installer.install()
    installer.copy_configs()
