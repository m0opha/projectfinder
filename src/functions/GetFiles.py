from .modules import ProgressBarLogger, Incrementor

def GetFiles(files_found:list,filename:str):

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Search for project files")

    total_files = len(files_found)

    files_use = Incrementor()    
    incrementor = Incrementor()
    
    files = []

    try:
        for _file in files_found:
            file_name = _file.split("/")[-1]
            
            if file_name == filename:   
                progress_logger.drawProgressBar(int(incrementor.get()*100/total_files))
                progress_logger.log(f"[+] {_file}")
                files_use.increment()
                files.append(_file)
        
            incrementor.increment()
   
    except KeyboardInterrupt:
        pass

    finally:
        progress_logger.close()

    return files
