"""
Run a Vapor script:      python main.py examples/hello.vp
Start the Vapor prompt:  python main.py
"""

import sys

from vapor.cli import main

if __name__ == "__main__":
    sys.exit(main())
