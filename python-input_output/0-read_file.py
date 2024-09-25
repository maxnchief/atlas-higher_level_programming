#!/usr/bin/python3
'''will open the file'''


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        
      
        '''prints the contents of the utf-8 file to stdout'''
    content = file.read()
    print(content, end='')
    
