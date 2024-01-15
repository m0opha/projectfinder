import json

from .modules import ProgressBarLogger, Incrementor

def ReadFiles(files:list):

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Find projects paths")   
    incrementor = Incrementor()
    total_files = len(files)
    content_files = []
    
    for _file in files:
        try:
            with open(_file, 'r') as file:
                contenido = file.read()
                file_content = json.loads(contenido)
                content_files.append(file_content)
            
            incrementor.increment()
   
            progress_logger.drawProgressBar(int(incrementor.get()*100/total_files))
            progress_logger.log(f"[+] {_file}")
        except:
            pass

        finally:
            progress_logger.close()

    return content_files