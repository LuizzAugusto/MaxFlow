import MaxFlow
import SimpleFile
import json

state = {
    'on':True,
    'help': \
        "start -> Start algorithm\n" + \
        "clear -> clear terminal" + \
        "open {path} -> Open file\n" + \
        "exit -> Exit program\n" + \
        "help -> Show this message"
}

def start(*args):
    MaxFlow.start()

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

instructionSet = {
    'start':start,
    'clear':clear,
    'exit':off,
    'open':openJson,
    'help':helpMsg
}