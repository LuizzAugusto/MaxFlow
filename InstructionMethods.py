# It's distributed under the MIT license (https://choosealicense.com/licenses/mit/)

import MaxFlow
import SimpleFile
import json
import txt2json

state = {
    'on':True,
    'help': \
        "start {initial_vertex finish_vertex}-> Start algorithm\n" + \
        "open -> Open json file\n" + \
        "clear -> clear terminal\n" + \
        "open {path} -> Open file\n" + \
        "exit -> Exit program\n" + \
        "txt2json -> Converts structured txt to json\n" + \
        "help -> Show this message"
}

def start(*args):
    MaxFlow.start(str(args[1]), str(args[2]))

def clear(*args):
    print('\033c')

def openJson(*args):
    try:
        filename = args[1]
        text = SimpleFile.read(filename)
        MaxFlow.state['json'] = json.loads(text)
        print(MaxFlow.state['json'])
    except Exception:
        print("Can't open file.")

def off(*args):
    global state

    print('Exit program')
    state['on'] = False

def helpMsg(*args):
    print(state['help'])

def convertion(*args):
    filename = args[1]
    txt2json.execute(filename)

instructionSet = {
    'start':start,
    'clear':clear,
    'exit':off,
    'open':openJson,
    'help':helpMsg,
    'txt2json':convertion
}