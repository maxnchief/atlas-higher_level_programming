#!/usr/bin/python3
'''will open the file'''


def read_file(filename=""):
    '''prints the contents of the utf-8 file to stdout'''
    with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content, end='')
    
