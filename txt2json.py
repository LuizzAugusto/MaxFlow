#! /usr/bin/env python3
from sys import argv as arguments
import SimpleFile
import re
import json

def execute(filename):
    text = _load_file(filename)

    if text:
        text = _pre_processing(text)
        json_dict = convertion(text)
        json_string = json.dumps(json_dict)
        SimpleFile.write(filename[:-3] + 'json', json_string)

def _load_file(filename):
    text = SimpleFile.read(filename)

    if text != None:
        return text
    else:
        print('Error, file not found!')
        return None

def _pre_processing(text):
    new_text = ''

    while text[-1] == '\n' or text[-1] == ' ':
        text = text[:-1]

    for line in text.split('\n'):
        line = re.sub('[^(0-9)]*', '', line, count=1)
        
        while line[-1] == ' ':
            line = line[:-1]
        
        new_text += line + '\n'

    new_text = new_text[:-1]
    
    return new_text

def convertion(text):
    json_dict = {}

    for line in text.split('\n'):
        splitted_line = line.split(' ')
        vertex = splitted_line[0]
        next_vertex = splitted_line[1]
        flow = int(splitted_line[2])

        if vertex not in json_dict:
            json_dict[vertex] = {}
        
        json_dict[vertex][next_vertex] = flow
    
    json_dict = add_zero(json_dict)
    return json_dict

def add_zero(json_dict):
    for vertex in json_dict:
        for next_vertex in json_dict[vertex].keys():
            if vertex not in json_dict[next_vertex].keys():
                json_dict[next_vertex][vertex] = 0
    
    return json_dict

if __name__ == '__main__' and len(arguments) > 1:
    execute(arguments[1])
