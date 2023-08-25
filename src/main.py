import os
from classes.directory_manager import DirectoryManager
from classes.git_manager import GitManager

path = os.getcwd()
directory_manager = DirectoryManager(path)
git_manager = GitManager(path)

# first_level_folders = ["data", "docs",
#                        "models", "notebooks", "reports", "src"]


# directory_manager.createDirectories(first_level_folders)
git_manager.add_into_local_repos()
git_manager.add_commit()
git_manager.push_to_remote()
