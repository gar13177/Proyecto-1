from antlr4 import *
from BayesGrammarLexer import BayesGrammarLexer
from BayesGrammarParser import BayesGrammarParser
from MyCode import BayesListener
from BayesianNetwork import BayesianNetwork

from BayesGrammarUserLexer import BayesGrammarUserLexer
from BayesGrammarUserParser import BayesGrammarUserParser
from MyCode2 import BayesUserListener


string ="""
p(a)=0.3 
p(b)=0.6 
p(c|a)=0.8
p(c|!a)=0.4
p(d|a,b)=0.7 
p(d|a,!b)=0.8 
p(d|!a,b)=0.1
p(d|!a,!b)=0.2
p(e|c)=0.7 
p(e|!c)=0.2
"""
"""
P(A)=0.3
P(B) = 0.23
P(C|A,B)=0.2
P(C|!A,B) = 0.1
P(C|A,!B)=0.77
P(C|!A,!B)=0.5
"""
"""
p(S) = 0.07
P(A) = 0.01
P(F | S, A) = 1.0
P(F | !S, A) = 0.9
P(F | S, !A) = 0.7
P(F | !S, !A) = 0.10
"""

lexer = BayesGrammarLexer(InputStream(string))
stream = CommonTokenStream(lexer)
parser = BayesGrammarParser(stream)
tree = parser.program()
printer = BayesListener()
walker = ParseTreeWalker()
walker.walk(printer, tree)

#print "probabilidades"
#for probability in printer.probabilities:
    #print probability
#print printer.variables

bn = BayesianNetwork(printer.probabilities, printer.variables)
if bn.hasError:
    print bn.error
else:
    string = "p(c|!a,e)"
    lexer = BayesGrammarUserLexer(InputStream(string))
    stream = CommonTokenStream(lexer)
    parser = BayesGrammarUserParser(stream)
    tree = parser.program()
    printer = BayesUserListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print bn.enumeration(printer.probability, printer.variables)


