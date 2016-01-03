#!/usr/bin/python

import sys, os, os.path, getopt
from os import walk
def main(argv,app_name):
    ##Check the input

    outputfile = "";
    try:
        opts, args = getopt.getopt(argv,"ho:",["long","help","ofile="])
    except getopt.GetoptError:
        disp_usage(app_name)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            disp_usage(app_name+'2')
            print 'Options:\n -h, -o <outputfile>; Long options: --help, --ofile <outputfile>,\n --long "This will make it load in the images..... some other way....."'
        elif opt in ("-o","--ofile"):
            #ADD FILENAME CHECK HERE!!
            print "ofile="+arg
            outputfile = os.path.dirname(os.path.realpath("./"))+"/"+arg;
        else:
            assert False, "unhandled option"
    if outputfile == "":
        print "You have to choose a outputfile! \n"
        disp_usage(app_name)
        sys.exit()
    make_list();

def disp_usage(app_name):
    print 'usage: '+app_name+' [options] [long options]\n type "'+app_name+' -h" for help'

def make_list():
    files = []
    dirs = []
    dir_path = []
    for (dirpath, dirnames, filenames) in walk("./"):
        files.extend(filenames)
        dirs.extend(dirnames)
        dir_path.extend(dirpath);
        break
    print files
    print dirs
    print dir_path


    #for root, _, files in os.walk("./"):
    #    for f in files:
    #        fullpath = os.path.join(root, f)
    #        #if os.path.getsize(fullpath) < 200 * 1024:
    #        #    os.remove(fullpath)
    #        print fullpath;


if __name__ == "__main__":
   main(sys.argv[1:],sys.argv[0])
