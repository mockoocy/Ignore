import sys
from typing import List

from src.lang.Driver import traverse

def exception_hook(exception_type, exception, traceback):
    print(exception)

sys.excepthook = exception_hook

def main(argv: List[str]) -> None:
    traverse(argv[1])


if __name__ == "__main__":
    main(sys.argv)
