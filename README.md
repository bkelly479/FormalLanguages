# Formal Languages and Computability Final project

This project was created for the final project of my Formal languages class. It is an implementation of grep based on a provided regex file. The regex file is then turned into a Non-deterministic Finite Automata, or NFA, using Thompson's algorithm. The NFA is turned into a DFA and the DFA is tested against lines in a provided file. If a match is found the line is returned. the DFA and NFA can also be output as a .dot file and .pdf file.

## Usage

### To run the grepy utility
```
py -3 .\grepy.py  a*b* testFile.txt
```

### To run the utility and create a DFA and NFA
```
py -3 .\grepy.py -d DFA.dot -n NFA.dot a*b* testFile.txt
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
