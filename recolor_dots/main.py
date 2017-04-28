"""
Usage: recolor COLORFILE [-h] [-i INDIR] [-o OUTDIR]

  -h --help                         show this screen
  -i INDIR --in_directory=INDIR     read dotfile templates from INDIR
  -o OUTDIR --out_directory=OUTDIR  write dotfiles to OUTDIR
"""
from docopt import docopt

import os
import pystache
import yaml

def parse_args(arguments):
    """
    Parse the docopt output.

    params:
    arguments: the docopt output dictionary

    returns:
    colorfile: the YAML file containing a colorscheme specification
    indir: the directory to read templates from
    outdir: the directory to write outputs to
    """
    colorfile = arguments['COLORFILE']
    if arguments['--in_directory']:
        indir = arguments['--in_directory']
    else:
        indir = '.'
    if arguments['--out_directory']:
        outdir = arguments['--out_directory']
    else:
        outdir = 'out'
    indir = os.path.abspath(indir)
    outdir = os.path.abspath(outdir)
    return colorfile, indir, outdir

def read(colorfile):
    """
    Read YAML file colorfile and represent it as a dictionary.

    params:
    colorfile: the YAML file containing a colorscheme specification

    Each line in colorfile must be one of 'base00: "xxxxxx"', ...,
    'base0F': "xxxxxx"'.

    returns:
    _dict: the hash corresponding to colorfile
    """
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

    Each tag must be one of '{{base00}}', ..., '{{base0F}}'.
    """
    with open(infile, 'rb') as f:
        render = pystache.render(f.read().decode('utf-8'), _dict)
    with open(outfile, 'wb') as f:
        f.write(render.encode('utf-8'))

def write_all(_dict, indir, outdir):
    """
    Apply _dict to the content of each file in indir and write the result to a
    corresponding file in outdir.

    params:
    _dict: the hash to apply
    indir: the directory to read templates from
    outdir: the directory to write outputs to
    """
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
