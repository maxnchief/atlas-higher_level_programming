#!/usr/bin/python3
'''
function will open the file
'''

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        
        '''
        this function opens a file and reads it
        '''

    content = file.read()
    print(content, end='')
    