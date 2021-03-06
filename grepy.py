#!/use/bin/env py -3



#import required modules

#will need to pip install these ones
# pip install automata-lib
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
#pip install graphviz
from graphviz import Digraph

#not these ones
import thompsonsAlg
import dot
import re
#import os
import argparse

#create commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--NFA", help="location to which NFA file will be output")
parser.add_argument("-d", "--DFA", help="location to which DFA file will be output")
parser.add_argument("REGEX")
parser.add_argument("FILE")
args = parser.parse_args()

#Fixes an error graphviz throws if you don't add it to path
#started working on this and realized involving os is probably a bad idea
#if you're getting that error maybe uncomment this

#if(args.ERROR):
#    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/graphviz-2.38/bin'
#else:
#    pass



#get file
inputFile = open(args.FILE, "r")
inputLines = inputFile.readlines()
regexToMatch = args.REGEX


#thompson alg output returns a NFA transition table
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

#check for NFA and DFA and generate DOT files also outputs a PDF of the same name
if(args.DFA):
    #makes sure it ends with the right file type
    if(not args.DFA.endswith(".dot")):
        fileName = args.DFA + ".dot"

        dot.graphDFA(dfa, fileName)
    else:
        dot.graphDFA(dfa, args.DFA)
else:
    pass

if(args.NFA):
    if(not args.NFA.endswith(".dot")):
        fileName = args.NFA + ".dot"

        dot.graphNFA(dfa, fileName)
    else:
        dot.graphNFA(dfa, args.NFA)


for line in inputLines:
    #steralize stuff like /n or /r
    line = ''.join(c for c in line if c.isprintable())
    try:
        #check DFA if it works print it
        if(dfa.accepts_input(line)):
            print(repr(line))
    except:
        pass
