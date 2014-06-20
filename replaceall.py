# -*- coding: utf-8 -*-
import sys
import os
import ntpath
import shutil

def main(source_dir, target_dir):
    files = []

    for f in get_abs_file_paths(source_dir):
        files.append(f)

    for f in files:
        target_file = find_file(target_dir, ntpath.basename(f))
        replace_file(f, target_file)

    print "## done ##"

def get_abs_file_paths(_dir):
   for root, dirs, files in os.walk(_dir):
       for f in files:
           yield os.path.abspath(os.path.join(root, f))

def find_file(_dir, filename):
    for root, dirs, files in os.walk(_dir):
        for f in files:
            if f == filename:
                 print 'got it, ', f
                 return os.path.abspath(os.path.join(root, f))

def replace_file(source_file, target_file):
    shutil.copy(source_file, target_file)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "error, using this script as same as the example: python replaceall.py test_data/source_dir/ test_data/target_dir/"
        sys.exit()
        
    sys.exit(main(sys.argv[1], sys.argv[2]))
