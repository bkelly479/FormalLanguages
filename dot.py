from graphviz import Digraph

def graphNFA(NFA):
    f = Digraph('NFA', filename='nfa.dot')

    f.attr(rankdir='LR', size='8,5')
    
    for state in NFA.states:
        if(state in NFA.final_states):
            f.attr('node', shape='doublecircle')
            f.node(state)
        else:
            f.attr('node', shape='circle')
            f.node(state)

    print((NFA.transitions))
    t = NFA.transitions

    for key in t: #n^3 that's rough
        print(key)
        for transCharacter in t[key]:
            print(transCharacter)
            for endLoc in t[key][transCharacter]:
                print(endLoc)
                if (transCharacter == ''):
                    transCharacter = 'Epsilon'
                f.edge(key, endLoc, label= transCharacter)

    f.view()

def graphDFA(DFA):
    f = f = Digraph('DFA', filename='DFA.dot')

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

    #print(stateDict)
    #print((DFA.transitions))
    t = DFA.transitions
    print(DFA.final_states)

    for key in t: #n^3 that's rough
        #print(key)
        #print(t[key])
        #print()
        for transCharacter in t[key]:
            print(transCharacter)
            print(stateDict[t[key][transCharacter]])
            f.edge(stateDict[key], stateDict[t[key][transCharacter]], label=transCharacter)
            #for endLoc in t[key][transCharacter]:
                #print(endLoc)
                #f.edge(stateDict[key], endLoc, label= transCharacter)

    f.render()