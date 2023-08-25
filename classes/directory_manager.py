import os
import requests


class DirectoryManager:
    def __init__(self, path):
        self.path = path

    def createEmptyDirectories(self, folders=[]):
        for folder in folders:
            os.makedirs(os.path.join(self.path, folder))
            with open('.gitkeep', 'w') as f:
                f.write('')

    def createFile(self, file, content=''):
        file_path = os.path.join(self.path, file)
        with open(file_path, 'w') as f:
            f.write(content)
