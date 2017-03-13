# Generated from BayesGrammarUser.txt by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\fN\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2")
        buf.write(u"\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write(u"\3\t\3\n\3\n\3\13\6\13-\n\13\r\13\16\13.\3\13\3\13\3")
        buf.write(u"\f\3\f\3\f\3\f\7\f\67\n\f\f\f\16\f:\13\f\3\f\5\f=\n\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\7\fD\n\f\f\f\16\fG\13\f\3\f\3\f")
        buf.write(u"\5\fK\n\f\3\f\3\f\3E\2\r\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write(u"\2\21\t\23\n\25\13\27\f\3\2\5\4\2C\\c|\5\2\13\f\16\17")
        buf.write(u"\"\"\4\2\f\f\17\17Q\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write(u"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\21\3\2\2\2")
        buf.write(u"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\3\31\3\2\2\2")
        buf.write(u"\5\33\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r")
        buf.write(u"#\3\2\2\2\17%\3\2\2\2\21\'\3\2\2\2\23)\3\2\2\2\25,\3")
        buf.write(u"\2\2\2\27J\3\2\2\2\31\32\7R\2\2\32\4\3\2\2\2\33\34\7")
        buf.write(u"r\2\2\34\6\3\2\2\2\35\36\7*\2\2\36\b\3\2\2\2\37 \7+\2")
        buf.write(u"\2 \n\3\2\2\2!\"\7~\2\2\"\f\3\2\2\2#$\7.\2\2$\16\3\2")
        buf.write(u"\2\2%&\t\2\2\2&\20\3\2\2\2\'(\7#\2\2(\22\3\2\2\2)*\5")
        buf.write(u"\17\b\2*\24\3\2\2\2+-\t\3\2\2,+\3\2\2\2-.\3\2\2\2.,\3")
        buf.write(u"\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\b\13\2\2\61\26\3\2")
        buf.write(u"\2\2\62\63\7\61\2\2\63\64\7\61\2\2\648\3\2\2\2\65\67")
        buf.write(u"\n\4\2\2\66\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2")
        buf.write(u"\2\29<\3\2\2\2:8\3\2\2\2;=\7\17\2\2<;\3\2\2\2<=\3\2\2")
        buf.write(u"\2=>\3\2\2\2>K\7\f\2\2?@\7\61\2\2@A\7,\2\2AE\3\2\2\2")
        buf.write(u"BD\13\2\2\2CB\3\2\2\2DG\3\2\2\2EF\3\2\2\2EC\3\2\2\2F")
        buf.write(u"H\3\2\2\2GE\3\2\2\2HI\7,\2\2IK\7\61\2\2J\62\3\2\2\2J")
        buf.write(u"?\3\2\2\2KL\3\2\2\2LM\b\f\2\2M\30\3\2\2\2\b\2.8<EJ\3")
        buf.write(u"\b\2\2")
        return buf.getvalue()


class BayesGrammarUserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    NEGATION = 7
    TOKEN = 8
    WS = 9
    COMMENT = 10

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'P'", u"'p'", u"'('", u"')'", u"'|'", u"','", u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"NEGATION", u"TOKEN", u"WS", u"COMMENT" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"LETTER", u"NEGATION", u"TOKEN", u"WS", u"COMMENT" ]

    grammarFileName = u"BayesGrammarUser.txt"

    def __init__(self, input=None):
        super(BayesGrammarUserLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


