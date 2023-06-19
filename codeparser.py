import os
import json
from pathlib import Path
from collections import deque
from queue import LifoQueue
from ringqueue.circularqueue import ringQueue

#Reader

def input_reader(file_path):
    code_stack = []

    source_code = Path(file_path).read_text()
    store_lenght = 0
    
    for character in source_code:
        if character != source_code[-1]:
            print(character)
            code_stack.append(character)
        
            #print(source_code[-1])
            #print('going')
        else:
            print('end')
            #first_100_char = source_code[:500]
            #circ_queue = ringQueue(100)
            #print(type(source_code))
    
            #circ_queue.decide_circular(first_100_char)
    print(code_stack)

def code_lexer(read_input):
    code_imput =  read_input

    def peek_lex(code_input):
        return code_imput
    
    def consume_lex(cons_lex):
        return cons_lex
    
    def lex_eof():
        return False

def code_parser(tokens):
    lexed_tokens = tokens


def error_handling(case_errors):
    return case_errors


input_reader('files/actual_response.json')