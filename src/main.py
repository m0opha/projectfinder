import json

from .functions import ArgHandler, CopyFoldersTo, ReadFiles, GetFiles,ExtractPaths
from .functions.modules import TraverseDirectoryTree

def main():
    filename = "projectfinder.json"
    path , destine = ArgHandler()
    project_files_path = GetFiles(files_found=TraverseDirectoryTree(path), filename=filename)
    file_content = ReadFiles(project_files_path)
    folder_to_copy = ExtractPaths(content=file_content, key="path")
    print(json.dumps(folder_to_copy, indent=2))

    CopyFoldersTo(folder_to_copy, destine)
    
    print(f"Total Project found : {len(folder_to_copy)}")