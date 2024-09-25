#!/usr/bin/python3
''' this file will write content to file'''

def write_file(filename="", text=""):
    '''function will write content to utf8 file'''
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(content)
        return len(content)