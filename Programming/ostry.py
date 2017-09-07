import os
import sys
filename = sys.argv[1]
if not os.path.isfile(filename):
    print "Sorry no this file"
    exit(0)
if not os.access(filename, os.R_OK):
    print "oops no access"
    exit(0)
print "yesyes, all passed for   " + filename
