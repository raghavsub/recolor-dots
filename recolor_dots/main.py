"""
Usage: recolor COLORFILE [-h] [-i INDIR] [-o OUTDIR]

  -h --help                         show this screen
  -i INDIR --in_directory=INDIR     read dotfile templates from INDIR
  -o OUTDIR --out_directory=OUTDIR  write dotfiles to OUTDIR
"""
from __future__ import print_function

from docopt import docopt

import os
import pystache
import yaml

def parse_args(arguments):
    colorfile = arguments['COLORFILE']
    if arguments['-i']:
        indir = arguments['INDIR']
    else:
        indir = '.'
    if arguments['-o']:
        outdir = arguments['OUTDIR']
    else:
        outdir = 'out'
    indir = os.path.abspath(indir)
    outdir = os.path.abspath(outdir)
    return colorfile, indir, outdir

def read(colorfile):
    with open(colorfile, 'rb') as f:
        _dict = yaml.load(f)
    return _dict

def _write_one(_dict, infile, outfile):
    """
    Apply _dict to the content of infile and write the result to outfile.

    params:
    _dict: the hash to apply
    infile: the template path (file must exist)
    outfile: the output path (directory must exist)
    """
    with open(infile, 'rb') as f:
        render = pystache.render(f.read().decode('utf-8'), _dict)
    with open(outfile, 'wb') as f:
        f.write(render.encode('utf-8'))

def write_all(_dict, indir, outdir):
    for root, dirs, files in os.walk(indir):
        for name in files:
            relpath = os.path.relpath(os.path.join(root, name), indir)
            infile = os.path.join(indir, relpath)
            outfile = os.path.join(outdir, relpath)
            outfile_dir = os.path.dirname(outfile)
            if not os.path.isdir(outfile_dir):
                os.makedirs(outfile_dir)
            _write_one(_dict, infile, outfile) 

def main():
    arguments = docopt(__doc__)
    colorfile, indir, outdir = parse_args(arguments)
    _dict = read(colorfile)
    write_all(_dict, indir, outdir)
