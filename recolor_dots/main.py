"""
Usage: recolor COLORFILE [-hd DIR]

  -h --help                 show this screen
  -d DIR --directory=DIR    find dotfile templates in DIR
"""

from .docopt import docopt

def main():
    arguments = docopt(__doc__)
    print(arguments)
