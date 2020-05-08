#!/use/bin/env py -3

#import required modules 
import argparse
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
from graphviz import Digraph
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


#thompson alg output returns essentially a transition table
thompsonOutput = thompsonsAlg.thompsonsAlg(regexToMatch)

#outputs of the 5 touple
print(set(thompsonOutput.s.keys()))
print(set(thompsonOutput.keys))
print(type(thompsonOutput.s))
print(list(thompsonOutput.s.keys())[0])
print({list(thompsonOutput.s.keys())[len(list(thompsonOutput.s.keys())) -1]})

#let's try building an NFA!
naf = NFA(
    states=set(thompsonOutput.s.keys()),
    input_symbols= set(thompsonOutput.keys),
    transitions= thompsonOutput.s,
    initial_state= list(thompsonOutput.s.keys())[0],
    final_states= {list(thompsonOutput.s.keys())[len(list(thompsonOutput.s.keys())) -1]}
)

#check for NFA and DFA
if(args.DFA):
    print("DFA SPECIFIED")
if(args.NFA):
    print("NFA SPECIFIED")


#outputs mostly for testing atm 
print("S")
print(thompsonOutput.s)
print("KEYS")
print(thompsonOutput.keys)
print("INPUT SYMBOLS")
print(thompsonOutput.inputSymbols)