#! /usr/bin/env python3
import Input

def main():
    Input.InstructionMethods.clear()
    
    while(Input.InstructionMethods.state['on']):
        Input.terminal()

if __name__ == '__main__':
    main()