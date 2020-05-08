#!/use/bin/env py -3

#import required modules 
import argparse
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from graphviz import Digraph
import infixToPostfix
import thompsonsAlg

#create commandline arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--NFA", help="location to which NFA file will be output")
parser.add_argument("-d", "--DFA", help="location to shich DFA file will be output")
parser.add_argument("REGEX")
args = parser.parse_args()

#get regex
regexFile = open(args.REGEX, "r")
regexToMatch = regexFile.read()

#converts infix regex to postfix regex idk if i even need thins
infixObj = infixToPostfix.Convert(len(regexToMatch))
postfix = infixObj.infixToPostfix(regexToMatch)

#thompson alg output 
thompsonOutput = thompsonsAlg.thompsonsAlg(regexToMatch)

#check for NFA and DFA
if(args.DFA):
    print("DFA SPECIFIED")
if(args.NFA):
    print("NFA SPECIFIED")


#outputs mostly for testing atm 
print(regexToMatch)
print(postfix)
print("S")
print(thompsonOutput.s)
print("KEYS")
print(thompsonOutput.keys)
print("INPUT SYMBOLS")
print(thompsonOutput.inputSymbols)