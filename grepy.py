#!/use/bin/env py -3

#   I'll be honest this is not a great implementation
#   i used a library to do most of the DFA and NFA work which probably great
#   Additionally this doesn't take parens () into account 
#   messed up there totally forgot about that one     
#   other than that it's pretty decent code i don't write a ton of python so i'm kinda happy with it
#   
#
#
#

#import required modules 
import argparse
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from graphviz import Digraph
import thompsonsAlg
import dot
import re
#import os

#create commandline arguments 
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--NFA", help="location to which NFA file will be output")
parser.add_argument("-d", "--DFA", help="location to which DFA file will be output")
#parser.add_argument("-e", "--ERROR", help="If graphviz is throwing an error because it hasn't been added to path settig this will fix that")
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
    line = ''.join(c for c in line if c.isprintable())
    try:
        if(dfa.accepts_input(line)):
            print(repr(line))
    except:
        pass

