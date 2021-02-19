import os
import requests
import shutil

from pathlib import Path


class Provisioner:

    @staticmethod
    def copy_configs():
        os.mkdir('/home/vagrant/.config')
        os.mkdir('/home/vagrant/.config/Operator/') 
        os.mkdir('/home/vagrant/.config/Operator/workspace')
        os.mkdir('/home/vagrant/.config/Operator/workspace/adversary') 
        if os.path.isfile('/vagrant/configs/settings.yml'):
            shutil.copyfile('/vagrant/configs/settings.yml', '/home/vagrant/.config/Operator/settings.yml')
        if os.path.isfile('/vagrant/configs/schedules.yml'):
            shutil.copyfile('/vagrant/configs/schedules.yml', '/home/vagrant/.config/Operator/schedules.yml')
        for directory, subdirectories, files in os.walk('/vagrant/adversary'):
            for adversary in [f for f in files if f.endswith('.yml')]:
                print('[+] Found adversary: %s' % adversary)
                shutil.copyfile(os.path.join(directory, adversary), '/home/vagrant/.config/Operator/workspace/adversary/%s' % adversary)


if __name__ == '__main__':
    provisioner = Provisioner()
    provisioner.copy_configs()

