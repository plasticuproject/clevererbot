'''
A simple, CLI Cleverbot chat app for linux, using the cleverbotfree
API and espeak.

Copyright (C) 2018  plasticuproject@pm.me

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''

import cleverbotfree.cbfree
import os
import sys

cb = cleverbotfree.cbfree.Cleverbot()


def main():

    try:
        print('[-] Connecting to Cleverbot.com...')
        try:
            cb.browser.get(cb.url)
        except:
            print('\n[-] Cannot connect to CleverBot. Please check your')
            print('[-] connection and try again\n')
            cb.browser.close()
            sys.exit()
        print('[-] Have a conversation with CleverBot...')
        print('[-] Just type "quit" to end the conversation\n')
        os.system('espeak -v english-us "Have a conversation with me."')
        os.system('espeak -v english-us "I am kind of a jerk but, whatever."')
        while True:
            try:
                cb.get_form()
            except:
                cb.browser.close()
            userInput = input('\033[1;94m USER: \033[1;37m')
            if userInput == 'quit':
                break
            cb.send_input(userInput)
            bot = cb.get_response()
            print('\033[1;92m CLEVERBOT: \033[1;37m', bot) , os.system('espeak -v english-us "{}"' .format(bot))
        cb.browser.close()
    except KeyboardInterrupt:
        print('\n\n[-] Thanks for chatting!\n')
        sys.exit()


if __name__ == '__main__':
    main()
