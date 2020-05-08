import re
import json

class ThompsonNFA:
    def __init__(self, s, keys, inputSymbols):
        self.s = s
        self.keys = keys
        self.inputSymbols = inputSymbols

def thompsonsAlg(postfix):
    regex=''.join(postfix)

    keys=list(set(re.sub('[^A-Za-z0-9]+', '', regex)+'e'))

    s={}
    stack=[]
    start=0
    end=1

    counter = 0
    currentState = 0
    lastInputSymbol = ''
    
    inputSymbols = []

    #assume we get a valid regex and will create an NFA
    s['q' + str(currentState)] = {'': {'q' + str(currentState + 1)}}
    currentState += 1

    print("REGEX IN THOMPSON ALG: " + regex)


    for i in regex:
        if i in keys:
            #i must be alphanumeric and must be a part of the alphabet
            inputSymbols.append(i)

            #create a state within s that goes from q(CURRENTSTATE) to q(CURRENTSTATE + 1) on i
            s['q' + str(currentState)] = {i : {'q' + str(currentState + 1)}}

            #record last input symbol
            lastInputSymbol = i

            #incriment current state 
            currentState += 1

        elif i == '*':

            #this is hacky and not technically right but i'm assuming a * or + has to come
            #after an input symbol this isn't right but the world ended like 2 months ago so whatever
            
            #remove the previous state
            del s['q' + str(currentState - 1)]
            #add a spontaneous transition to the current state and state two later
            s['q' + str(currentState - 1)] = {'' : {('q' + str(currentState)), ('q' + str(currentState + 2)) }}
            #add current state going to current state + 1 on last Input Symbol
            s['q' + str(currentState)] = {lastInputSymbol : {'q' + str(currentState + 1)}}
            #next state can transition back to current state and forward to currentState + 2
            s['q' + str(currentState + 1)] = {'': {('q' + str(currentState)), ('q' + str(currentState + 2))}}
            
            #incriment current state twice, currentState+2 doesn't exist ATM but will be created
            #either by the next i or by the line adding a final state at the end
            currentState += 2
        elif i == '+':

            #this will be simmilar to the * but with fewer spontaneous transitions 
            
            #remove the previous state
            del s['q' + str(currentState - 1)]
            s['q' + str(currentState - 1)] = {'' : {'q' + str(currentState)}}
            s['q' + str(currentState)] = {lastInputSymbol : {'q' + str(currentState + 1)}}
            s['q' + str(currentState + 1)] = {'' : {('q' + str(currentState)),('q' + str(currentState + 2))}}

            currentState += 2
            
        else:
            pass

    """for i in regex:
        if i in keys:
            c0=c0+1
            c1=c0
            c0=c0+1
            c2=c0

            s.append({})
            s.append({})
            stack.append([c1,c2])
            s[c1][i]=c2

        elif i=='*':
            r1,r2=stack.pop()
            c0=c0+1;c1=c0;c0=c0+1;c2=c0
            s.append({});s.append({})
            stack.append([c1,c2])
            s[r2]['e']=(r1,c2);s[c1]['e']=(r1,c2)
            if start==r1:start=c1 
            if end==r2:end=c2 
        elif i=='.':
            r11,r12=stack.pop()
            r21,r22=stack.pop()
            stack.append([r21,r12])
            s[r22]['e']=r11
            if start==r11:start=r21 
            if end==r22:end=r12 
        else:
            c0=c0+1;c1=c0;c0=c0+1;c2=c0
            s.append({});s.append({})
            r11,r12=stack.pop()
            r21,r22=stack.pop()
            stack.append([c1,c2])
            s[c1]['e']=(r21,r11); s[r12]['e']=c2; s[r22]['e']=c2
            if start==r11 or start==r21:start=c1 
            if end==r22 or end==r12:end=c2"""
    
    #add last accepting state 
    s['q' + str(currentState)] = {"FINAL STATE"}

    return ThompsonNFA(s, keys, inputSymbols)