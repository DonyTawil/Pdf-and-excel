#  This python file is used to modify the index in excel files
#  The input is a directory containing the index files

import openpyxl
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", required=True, \
                help="Directory containing index files to modify")
ap.add_argument("-p", "--prev",\
                required=False, default=None,\
                help="The previous index that were used in excel")
ap.add_argument("-i", "--index", required=True, help="The current index")
ap.add_argument("-a", "--at", required=True, help="The position of the index in the excel file" )



args= vars(ap.parse_args())

curIndex = args["index"]  # The index that we are currently at
filepath = args["dir"]  # The file path where the excels files are
prevIndex = args["prev"] # The previous index
posIndex = args["at"]  # The position of the index in excel e.g:A1

os.chdir(filepath)  # Change to the destination

files = os.listdir()

for file in files:
    
