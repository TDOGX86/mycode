#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
from colorama import Fore, Back, Style

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print(Fore.YELLOW + 'Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print(Fore.CYAN + 'Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

#fucntion for IP list
def devicereboot(devicecmd):
    for coffeetime in devicecmd.keys():
        print(Fore.RED + 'Connecting to-->'+ coffeetime + ' REBOOTING NOW!')

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print(Fore.BLUE + "Welcome to the network device command pusher") # welcome message

    ## get data set
    print(Fore.GREEN + "\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

    devicereboot(work2do)

# call our main function
main()

