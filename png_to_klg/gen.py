#!/usr/bin/python

##  Author: Jacky Liu
##    Date: 7 Dec 2016

from os import listdir
from os.path import isfile, join
import sys
import re


def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]
 
def timeFile(fileList, path, subfolder):
    file_name = path + '/' + subfolder + '.txt'
    fp = open(file_name, 'w')
    
    count = 0.033333
    
    for fileName in fileList:
        fp.write("%.6f %s/%s\n" % (count, subfolder, fileName))
        count = count + 0.033333
    
    fp.close()
    return file_name

def getDataTxt(mypath):
    rgbfiles = [f for f in listdir(mypath+'/rgb') if isfile(join(mypath+'/rgb', f))]
    depthfiles = [f for f in listdir(mypath+'/depth') if isfile(join(mypath+'/depth', f))]

    intersection = list(set(rgbfiles) & set(depthfiles))

    intersection.sort(key=natural_key)
    #print(onlyfiles)
    
    rgb_file = timeFile(intersection, mypath, 'rgb')
    depth_file = timeFile(intersection, mypath, 'depth')
    return rgb_file, depth_file


if __name__ == "__main__":
        #mypath = './rgb'
    if len(sys.argv) < 2:
        print("please input folder path, >python ./gen.py ./dir\ndir contains rgb and depth folder")
        sys.exit(1)

    mypath = sys.argv[1]
    print(mypath)
    getDataTxt(mypath)

