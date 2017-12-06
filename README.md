# Introduction
guetzed is a python wrapper for guetzli. [Guetzli](https://github.com/google/guetzli) is a Google alogrithm to optimize JPEG and PNG images, processing one file at a time. guetzed automates the compression of JPEGs and PNGs found recursively. By default guetzed keep a copy of the original files an process both JPEGs and PNGs within a given folder.

By default, guetzed keeps a copy of the original files, appending the `.bkp` extension to the filename. The scripts operates either in the directory where it is executed.

## Linux install
1. Install `guetzli` and `argparse` for python3 via your favorite method
2. Copy `guetzed` to /usr/bin

## Usage
guetzed [-h] [-i INPUT] [-o OUTPUT] [-q QUALITY] [-j] [-p] [-d] [-v]

### Parameters ###
By default, guetzed uses the followign options:
- execution folder is where the script is exectued

- output folder is identical as original image folder

- JPGs are compressed, backup copies of the original are kept 

- PNGs are converted to JPGs, then compressed, the originals are ketp

- quality level is set to 90

### Flag ###
-h, --help                    show this help message and exit
-j, --jpeg                    recompress ONLY JPG (by default it will also recompress PNG)
-p, --png                     recompress ONLY PNG (by default it will also recompress JPG)
-d, --delete                  delete the original file after conversion. By default keep a backup
-v, --verbosity               increase output verbosity
-i INPUT, --input INPUT       <folder> specify a folder of images to recompress. Default folder is where the script is executed
-o OUTPUT, --output OUTPUT    <folder> specify a folder for the recompressed images. By default, same folder as original image
-q QUALITY, --quality QUALITY <int> specify quality, 0-100, default 90

### Example Usage
Replace all files at quality 90 :

`guetzed`

Convert PNGs at quality 95, and remove original:

`guetzed -q 95 -p -d`

Convert only JPGs from folder /home/megavolts/Download in /home/megavolts/Desktop and remove originals

`guetzed -j -i /home/megavolts/Desktop -o /home/megavolts/Desktop`

## Ressources
- [Guetzli](https://github.com/google/guetzli)
- [Guetzling](https://github.com/lejacobroy/Guetzling), a bash wrapper for guetzli
