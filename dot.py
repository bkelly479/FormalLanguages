from graphviz import Digraph

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/graphviz-2.38/bin'

def graphNFA(NFA, fileName):
    f = Digraph('NFA', filename=fileName)

    f.attr(rankdir='LR', size='8,5')
    
    for state in NFA.states:
        if(state in NFA.final_states):
            f.attr('node', shape='doublecircle')
            f.node(state)
        else:
            f.attr('node', shape='circle')
            f.node(state)

    t = NFA.transitions

    for key in t: #n^3 that's rough
        for transCharacter in t[key]:
            for endLoc in t[key][transCharacter]:
                if (transCharacter == ''):
                    transCharacter = 'Epsilon'
                f.edge(key, endLoc, label= transCharacter)

    f.render()

def graphDFA(DFA, fileName):
    f =  Digraph('DFA', filename=fileName)

    f.attr(rankdir='LR', size='8,5')


    stateCounter = 0
    stateDict = {}
    for state in DFA.states:
        stateDict[state] = 'q' + str(stateCounter)
        stateCounter += 1
        if(state in DFA.final_states):
            f.attr('node', shape='doublecircle')
            f.node(stateDict[state])
        else:
            f.attr('node', shape='circle')
            f.node(stateDict[state])

    t = DFA.transitions

    for key in t: #n^2 better but not great
        for transCharacter in t[key]:
            f.edge(stateDict[key], stateDict[t[key][transCharacter]], label=transCharacter)

    f.render()