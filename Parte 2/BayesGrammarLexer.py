# Generated from BayesGrammar.txt by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\17^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4")
        buf.write(u"\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write(u"\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17=\n\17")
        buf.write(u"\r\17\16\17>\3\17\3\17\3\20\3\20\3\20\3\20\7\20G\n\20")
        buf.write(u"\f\20\16\20J\13\20\3\20\5\20M\n\20\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\7\20T\n\20\f\20\16\20W\13\20\3\20\3\20\5\20[\n")
        buf.write(u"\20\3\20\3\20\3U\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write(u"\n\23\2\25\2\27\13\31\f\33\r\35\16\37\17\3\2\5\4\2C\\")
        buf.write(u"c|\5\2\13\f\16\17\"\"\4\2\f\f\17\17`\2\3\3\2\2\2\2\5")
        buf.write(u"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write(u"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write(u"\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2")
        buf.write(u"\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+\3")
        buf.write(u"\2\2\2\17-\3\2\2\2\21/\3\2\2\2\23\61\3\2\2\2\25\63\3")
        buf.write(u"\2\2\2\27\65\3\2\2\2\31\67\3\2\2\2\339\3\2\2\2\35<\3")
        buf.write(u"\2\2\2\37Z\3\2\2\2!\"\7R\2\2\"\4\3\2\2\2#$\7r\2\2$\6")
        buf.write(u"\3\2\2\2%&\7*\2\2&\b\3\2\2\2\'(\7+\2\2(\n\3\2\2\2)*\7")
        buf.write(u"?\2\2*\f\3\2\2\2+,\7~\2\2,\16\3\2\2\2-.\7\60\2\2.\20")
        buf.write(u"\3\2\2\2/\60\7.\2\2\60\22\3\2\2\2\61\62\t\2\2\2\62\24")
        buf.write(u"\3\2\2\2\63\64\4\62;\2\64\26\3\2\2\2\65\66\7#\2\2\66")
        buf.write(u"\30\3\2\2\2\678\5\23\n\28\32\3\2\2\29:\5\25\13\2:\34")
        buf.write(u"\3\2\2\2;=\t\3\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3")
        buf.write(u"\2\2\2?@\3\2\2\2@A\b\17\2\2A\36\3\2\2\2BC\7\61\2\2CD")
        buf.write(u"\7\61\2\2DH\3\2\2\2EG\n\4\2\2FE\3\2\2\2GJ\3\2\2\2HF\3")
        buf.write(u"\2\2\2HI\3\2\2\2IL\3\2\2\2JH\3\2\2\2KM\7\17\2\2LK\3\2")
        buf.write(u"\2\2LM\3\2\2\2MN\3\2\2\2N[\7\f\2\2OP\7\61\2\2PQ\7,\2")
        buf.write(u"\2QU\3\2\2\2RT\13\2\2\2SR\3\2\2\2TW\3\2\2\2UV\3\2\2\2")
        buf.write(u"US\3\2\2\2VX\3\2\2\2WU\3\2\2\2XY\7,\2\2Y[\7\61\2\2ZB")
        buf.write(u"\3\2\2\2ZO\3\2\2\2[\\\3\2\2\2\\]\b\20\2\2] \3\2\2\2\b")
        buf.write(u"\2>HLUZ\3\b\2\2")
        return buf.getvalue()


class BayesGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NEGATION = 9
    TOKEN = 10
    NUMBERS = 11
    WS = 12
    COMMENT = 13

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'P'", u"'p'", u"'('", u"')'", u"'='", u"'|'", u"'.'", u"','", 
            u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"NEGATION", u"TOKEN", u"NUMBERS", u"WS", u"COMMENT" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"T__6", u"T__7", u"LETTER", u"NUMBER", u"NEGATION", u"TOKEN", 
                  u"NUMBERS", u"WS", u"COMMENT" ]

    grammarFileName = u"BayesGrammar.txt"

    def __init__(self, input=None):
        super(BayesGrammarLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


