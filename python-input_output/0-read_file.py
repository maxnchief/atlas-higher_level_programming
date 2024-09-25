#!/usr/bin/python3
'''will open the file'''


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        
      
        '''
        this function opens a file and reads it
        Args:
            @filename - the name of the file being read
        '''


    content = file.read()
    print(content, end='')
    