import os
import json
from pathlib import Path
from collections import deque
from queue import LifoQueue

#Reader

def input_reader(file_path):
    code_stack = []

    mystack = deque()
    #mystack.append('')

    #lifo_stack = LifoQueue
    #lifo_stack.put('')
    #if os.path.isfile(file_path):
        #with open(file_path,'r')  as f:
            #.append(f)
            #val = f.peek()
            #print(type(val))
    source_code = Path(file_path).read_text()
    new_source_code_list = source_code.split(' ')
    buffer_length = len(new_source_code_list)
    print('buffer_length', buffer_length)
    for i in new_source_code_list:
        code_stack.append(i)
        

        #val = file_path.peek()
        #print(type(val))

    
    #print(mystack.peek())
    #print(len(mystack))
    #print(code_stack)


    #def peek(source_code):
        #return source_code
    
    #def consume(code_stack):
        #return code_stack
    
    #def end_of_file():
        #return False
    

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