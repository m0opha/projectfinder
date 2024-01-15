import sys

from .modules import parser
from ..variables import allowed_arg
from .help import help

def ArgHandler():
    arg_extract = parser()

    path = None
    destine_path = None

    if len(arg_extract) == 2:
        help()

    for _argv , _value in arg_extract.items():
        if _argv not in allowed_arg:
            print(f"[+] unrecognized argument {_argv}, use --help, -h")
            sys.exit()
        
        elif _argv in ["--help", "-h"]:
            help()

        elif _argv in ["--path", "-p"]:
            if len( _value) < 1:
                print(f"[-] You can only enter a single path in {_argv}")
                sys.exit()

            else:
                path = _value
        
        elif _argv in ["--destine", "-d"]:
            if len( _value) < 1:
                print(f"[-] You can only enter a single path {_argv}")
                sys.exit(1)

            else:
                destine_path = _value

    return path, destine_path