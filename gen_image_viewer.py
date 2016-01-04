#!/usr/bin/python

import sys, os, os.path, getopt
from os import walk

def main(argv,app_name):
    ##Check the input

    outputfile = ""
    #TODO make it possible to search other directory for example static dir
    #walk_dir = "./"
    try:
        opts, args = getopt.getopt(argv,"ho:",["long","help","ofile="])
    except getopt.GetoptError:
        disp_usage(app_name)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            disp_usage(app_name+'2')
            #TODO add a way to add domain before path
            print 'Options:\n -h, -o <outputfile>; Long options: --help, --ofile <outputfile>,\n --long "This will make it load in the images..... some other way....."'
        elif opt in ("-o","--ofile"):
            #ADD FILENAME CHECK HERE!!
            print "ofile="+arg
            outputfile = os.path.dirname(os.path.abspath(__file__))+"/"+arg;
            #outputfile = os.path.dirname(os.path.realpath("./"))+"/"+arg;
        else:
            assert False, "unhandled option"
    if outputfile == "":
        print "You have to choose a outputfile! \n"
        disp_usage(app_name)
        sys.exit()


    #Begin creation


    files, dirs = make_list();

    #Download files if missing
    if not os.path.isfile("file_viewer.js"):
        print "Missing file: file_viewer.js"
    if not os.path.isfile("image_viewer.js"):
        print "Missing file: image_viewer.js"

    make_index(outputfile,files,dirs);


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
    return (files,dirs)

    #for root, _, files in os.walk("./"):
    #    for f in files:
    #        fullpath = os.path.join(root, f)
    #        #if os.path.getsize(fullpath) < 200 * 1024:
    #        #    os.remove(fullpath)
    #        print fullpath;

def make_index(ofile,files,dirs):
    print ofile
    print files
    f = open(ofile,'w');
    with open("base_start.html") as base_start:
        for line in base_start:
            f.write(line)

    for obj in files:
        if ".jpg" in obj or ".gif" in obj:
            f.write('<tr><td><a class="to_img_viewer" href="'+obj+'">'+obj+'</a></td></tr>')

    with open("base_end.html") as base_end:
        for line in base_end:
            f.write(line)


if __name__ == "__main__":
   main(sys.argv[1:],sys.argv[0])
