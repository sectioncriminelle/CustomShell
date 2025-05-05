#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import platform
from colorama import Fore, init
init()

class devilshell:
    def __init__(self):
        self.running = True
        self.username = os.getenv('USERNAME', 'user')
        self.current_dir = os.getcwd()
        self.ascii_logo = f"""{Fore.MAGENTA}
                                ____  _______    ________   _____ __  __________    __ 
                               / __ \\/ ____/ |  / /  _/ /  / ___// / / / ____/ /   / / 
                              / / / / __/  | | / // // /   \\__ \\/ /_/ / __/ / /   / /  
                             / /_/ / /___  | |/ // // /______/ / __  / /___/ /___/ /___
                            /_____/_____/  |___/___/_____/____/_/ /_/_____/_____/_____/
                                                            {Fore.RESET}
"""
        self.commands = {
            "clear": self.cllear,
            "exit": self.quitt
        }

    def run(self):
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(self.ascii_logo)   
        while self.running:
            prompt = "> "
            command = input(prompt)
            self.current_dir = os.getcwd()
            
            if not command.strip():
                continue
            cmd_parts = command.strip().split()
            cmd_name = cmd_parts[0].lower()
            
            if cmd_name in self.commands:
                self.commands[cmd_name](cmd_parts[1:] if len(cmd_parts) > 1 else [])
            else:
                try:
                    result = subprocess.run(command, shell=True, text=True)
                except Exception as e:
                    print(f"{e}")

    def cllear(self, args):
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(self.ascii_logo)
        
    def quitt(self, args):
        self.running = False

if __name__ == "__main__":
    try:
        cmd = devilshell()
        cmd.run()
    except KeyboardInterrupt:
        print("\nClose Shell, bye !")
    except Exception as e:
        print(f"{e}")
