#!/bin/bash


test(){
    local output_folder=$1
    for i in {1..10}; do
        file_name="project-$i"
        mkdir $output_folder/$file_name
        json_content="{\"project_name\": \"$file_name\", \"path\": \"$output_folder/$file_name\"}"
        echo "$json_content" > "$output_folder/$file_name/projectfinder.json"
        echo "Archivo creado: $output_folder/$file_name/projectfinder.json"
    done
}

build_binary() {

    local pythonfile="$1"

    if ! command -v pyinstaller &> /dev/null; then
        echo "PyInstaller is not installed. Installing..."
        pip install pyinstaller
        echo "PyInstaller installed successfully."
    else
        echo "PyInstaller is already installed."
    fi

    pyinstaller --onefile -i NONE $pythonfile
}


while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -t|--test)
            echo "Create folder test..."
            test $2
            exit 0
            ;;
            
        -b|--build)
            echo "Building a binary of the project with pyinstaller..."
            build_binary "projectfinder.py"
            exit 0
            ;;

        -r|--run)
            if [ -f "./dist/projectfinder" ]; then
                echo "Running app..."
                ./dist/projectfinder 
            else
                echo "Executable not found. Building binary..."
                build_binary
                echo "Running app..."
                ./dist/projectfinder
            fi
            exit 0
            ;;
        *)
            echo "Invalid option: $1" >&2
            exit 1
            ;;
    esac
    shift
done