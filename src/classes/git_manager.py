import subprocess


class GitManager:
    def __init__(self, path):
        self.path = path

    def add_into_local_repos(self, filesToAdd='.'):
        subprocess.run(["git", "add", filesToAdd], cwd=self.path)

    def add_commit(self, message="Initial commit"):
        subprocess.run(["git", "commit", "-m", message], cwd=self.path)

    def push_to_remote(self, branch="main"):
        subprocess.run(["git", "push", "-u", "origin", branch], cwd=self.path)
