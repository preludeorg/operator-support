import os
import requests


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


if __name__ == '__main__':
    installer = Installer()
    installer.download()
    installer.install()

