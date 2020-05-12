from graphviz import Digraph

#creates NFA and DFA from NFA and DFA objects 

def graphNFA(NFA, fileName):
    #create diagram
    f = Digraph('NFA', filename=fileName)

    #set set options
    f.attr(rankdir='LR', size='8,5')
    
    #create nodes
    for state in NFA.states:
        #checks if state is final if so double circle else single circle
        if(state in NFA.final_states):
            f.attr('node', shape='doublecircle')
            f.node(state)
        else:
            f.attr('node', shape='circle')
            f.node(state)

    #easier to type
    t = NFA.transitions

    #this can definetly be done faster but i'm not great with python 
    for key in t: #n^3 that's rough
        for transCharacter in t[key]:
            for endLoc in t[key][transCharacter]:
                #uses the phrase 'Epsilon" instead of an empty string 
                if (transCharacter == ''):
                    transCharacter = 'Epsilon'
                    # I tried to use the epsilon character but python doesn't like unicode apparently
                
                #create edge from key to endLoc on transCharacter
                f.edge(key, endLoc, label= transCharacter)

    #render instead of view i don't like stuff popping up i'll open it myself
    #also this makes a PDF too which is easier to see
    f.render()


#pretty much the same as the other one but a couple extra bits i'll point out
def graphDFA(DFA, fileName):
    f =  Digraph('DFA', filename=fileName)

    f.attr(rankdir='LR', size='8,5')


    # creating the DFA from the NFA creates states that are the names of all the NFA states together
    # so this creates a translation dictionary that is O(n) to name the states as they come in
    # q0 is usually in the middle 
    stateCounter = 0
    stateDict = {}
    for state in DFA.states:

        #creates states
        stateDict[state] = 'q' + str(stateCounter)
        stateCounter += 1

        #if state is in final state double circle 
        if(state in DFA.final_states):
            f.attr('node', shape='doublecircle')
            f.node(stateDict[state])
        else: #else single circle
            f.attr('node', shape='circle')
            f.node(stateDict[state])

    #easier to type 
    t = DFA.transitions

    for key in t: #n^2 better but not great
        for transCharacter in t[key]:
            f.edge(stateDict[key], stateDict[t[key][transCharacter]], label=transCharacter)

    f.render()