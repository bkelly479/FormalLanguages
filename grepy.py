#!/use/bin/env py -3

import argparse

#create commandline arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-n")
parser.add_argument("-d")
parser.add_argument("REGEX")
args = parser.parse_args()

regexFile = open(args.REGEX, "r")


print(regexFile.read())