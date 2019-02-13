import subprocess
import os.path


def create_folder(root, path=None):
    """Creates a folder with the name 'root' either in the current folder if path is None or a specified path.

    Parameters
    ----------
    root : str
        The name of the created folder.
    path : str, optional
        The name of the path for the new folder.
    """
    if path is None:
        if os.path.isdir(root) is False:
            subprocess.call('mkdir ' + root, shell=True)
    else:
        if os.path.isdir(path+root) is False:
            subprocess.call('mkdir ' + path + root, shell=True)
