import shutil
import os
from .modules import Incrementor, ProgressBarLogger

def CopyFoldersTo(folders:list, destination:str):
    
    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] copying Folders to destination")    

    incrementor = Incrementor()
    total_folder = len(folders)

    for _folder in folders:
        try:
            shutil.copytree(_folder, os.path.join(destination, os.path.basename(_folder)))
            incrementor.increment()

            progress_logger.drawProgressBar(int(incrementor.get()*100/total_folder))
            progress_logger.log(f"Folder copied from {_folder} to {destination}")

        except Exception as e:
            print(f"Error copying the folder: {e}")
        
        finally:
            progress_logger.close()

    return incrementor.get()

