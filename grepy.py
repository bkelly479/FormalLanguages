#!/use/bin/env py -3

#import required modules 
import argparse
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from graphviz import Digraph
import thompsonsAlg
import dot
import re

#create commandline arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--NFA", help="location to which NFA file will be output")
parser.add_argument("-d", "--DFA", help="location to shich DFA file will be output")
parser.add_argument("REGEX")
parser.add_argument("FILE")
args = parser.parse_args()

#get regex
inputFile = open(args.FILE, "r")
inputLines = inputFile.readlines()
regexToMatch = args.REGEX


#thompson alg output returns essentially a transition table
thompsonOutput = thompsonsAlg.thompsonsAlg(regexToMatch)


#let's try building an NFA!
nfa = NFA(
    states=set(thompsonOutput.s.keys()),
    input_symbols= set(thompsonOutput.keys),
    transitions= thompsonOutput.s,
    initial_state= list(thompsonOutput.s.keys())[0],
    final_states= {list(thompsonOutput.s.keys())[len(list(thompsonOutput.s.keys())) -1]}
)

#build a DFA from NFA (wow i'm really trusting this library with my grade)
dfa = DFA.from_nfa(nfa)

#check for NFA and DFA
if(args.DFA):
    dot.graphDFA(dfa, args.DFA)
if(args.NFA):
    dot.graphNFA(nfa, args.NFA)


for line in inputLines:
    line = ''.join(c for c in line if c.isprintable())
    try:
        if(dfa.accepts_input(line)):
            print(repr(line))
    except:
        pass

#outputs mostly for testing atm 
#print("S")
#print(thompsonOutput.s)
#print("KEYS")
#print(thompsonOutput.keys)
#print("INPUT SYMBOLS")
#print(thompsonOutput.inputSymbols)
#print(inputFile)