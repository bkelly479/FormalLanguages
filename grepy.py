#!/use/bin/env py -3

#import required modules 
import argparse
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from graphviz import Digraph
import infixToPostfix

#create commandline arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--NFA", help="location to which NFA file will be output")
parser.add_argument("-d", "--DFA", help="location to shich DFA file will be output")
parser.add_argument("REGEX")
args = parser.parse_args()

regexFile = open(args.REGEX, "r")
regexToMatch = regexFile.read()

infixObj = infixToPostfix.Convert(len(regexToMatch))
postfix = infixObj.infixToPostfix(regexToMatch)

print(args.REGEX)
print(postfix)