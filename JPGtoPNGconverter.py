# Exercise: JPG to PNG Converter
# must be able to type from commandline the ff:
    # python3 JPGtoPNGconverter.py Pokedex\ new\
# grab the 1st and 2nd argument
# check if new folder exists, if not create it
# loop thru Pokedex
# convert images to PNG
# save them to the 'new' folders

import sys # grab the 1st and 2nd argument
import os # grab the path
from PIL import Image

# grab the 1st and 2nd argument
from_folder = sys.argv[1]
destination_folder = sys.argv[2]

if (from_folder):
    jpg_files = (os.listdir(from_folder))
    
    for file in jpg_files: # loop thru Pokedex
        if file.endswith(".jpg"):
            img = Image.open(os.path.join(from_folder, file))

            if (destination_folder): # user specified a destination folder
                filename = os.path.basename(file)
                basename = filename.split('.')[0]
                # check if new folder exists, if not create it
                if not os.path.exists(destination_folder): 
                    os.mkdir(destination_folder) # create new path
                
                pathname = destination_folder + basename
                img.save(pathname +'.png', 'png') # convert images to PNG
                    

