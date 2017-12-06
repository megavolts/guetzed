#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
from os import path, walk, remove, rename, getcwd
from imghdr import what
from shutil import copy2
from subprocess import call


parser = argparse.ArgumentParser(
    description="""guetzed is a python wrapper for guetyli. Guetlzi is a Google alogrithm to optimize JPEG and PNG images, processing one file at a time. guetzed automates the compression of JPEGs and PNGs found recursively. By default guetzed keep a copy of the original files an process both JPEGs and PNGs within a given folder.""")
parser.add_argument('-i', '--input',
    required=False,
    type=str,
    help="<folder> Speficify a folder of images to recompress. By default current folder",
    default=getcwd()
    )
parser.add_argument('-o', '--output',
    required=False,
    type=str,
    help="<folder> Speficify a folder for the recompressed images. By default current folder",
    default=None
    )
parser.add_argument('-q', '--quality',
    required=False,
    type=float,
    help="Specify quality, 80-100, default 90",
    default=90
    )
parser.add_argument('-j', '--jpeg',
    required=False,
    action="store_false",
    help="Recompress ONLY JPG (by default it will also recompress PNG)",
    default="True"
    )
parser.add_argument('-p', '--png',
    required=False,
    action="store_false",
    help="Recompress ONLY PNG (by default it will also recompress JPG)",
    default="True"
    )
parser.add_argument('-d', '--delete',
    required=False,
    action="store_true",
    help="Delete the original file after conversion. By default keep a backup",
    default="False"
    )
parser.add_argument('-v', '--verbosity',
    required=False,
    action="count",
    help="increase output verbosity",
    default=0
    )

def run():
    args = parser.parse_args()
    TYPES = ['jpeg', 'png']    
    if args.png is False:
        TYPES.remove('jpeg')
    if args.jpeg is False:
        TYPES.remove('png')
    if args.png is False and args.jpeg is False:
        print("Nothing to do")
        return 0

    file = []
    for dirpath, dirnames, files in walk(args.input):
        for name in files:
            if not name.endswith(".bkp"):
                filepath = path.join(dirpath, name)
                # Check type
                if what(filepath) in TYPES:
                    # Get filepaths
                    filepath_temp = path.join(dirpath, "temp.jpg")

                    # Execute guetzli
                    call(['guetzli', filepath, filepath_temp])

                    original_size = path.getsize(filepath)
                    compress_size = path.getsize(filepath_temp)
                    compress_ratio = (original_size-compress_size) / original_size * 100
                    
                    if compress_ratio < 0:
                        print("%s \t compress ratio: %.0f, keep original file" %(filepath, compress_ratio))
                        remove(filepath_temp)
                    else:
                        if args.delete is True:
                            remove(filepath)
                        else:
                            copy2(filepath, filepath+'.bkp')
                            remove(filepath)

                        if args.output is None:
                            filepath_out = path.join(dirpath, '.'.join(name.split('.')[:-1])+'.jpg')
                            ii=1
                            while path.exists(filepath_out):
                                filepath_out = path.join(dirpath, '.'.join(name.split('.')[:-1])+'-'+str(ii)+'.jpg')
                                ii = ii+1
                        else:
                            filepath_out = path.join(args.output, name)
                            ii=1
                            while path.exists(filepath_out):
                                filepath_out = path.join(args.output, '.'.join(name.split('.')[:-1])+'-'+str(ii)+'.jpg')
                                ii = ii+1
                        if args.verbosity > 0:
                            print("%s \t compress ratio: %.0f" %(filepath, compress_ratio))
                        copy2(filepath_temp, filepath_out)
                        remove(filepath_temp)
    return 0
run()
