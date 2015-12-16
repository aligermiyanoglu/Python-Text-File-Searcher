#!/usr/bin/python

# Copyright 2014, Gurobi Optimization, Inc.

##
# 	Ali Germiyanoglu
#
##
import sys
import os


def searchText(filename, text):
    try:
        os.remove("./shortLog.txt")
    except OSError:
        pass

    f = open('shortLog.txt','w')

    previousTenLine = []
    with open(filename, 'r') as inF:
        lineCounter = 0
        for line in inF:
            lineCounter = lineCounter + 1
            previousTenLine.append(line)
            if text in line:
                f.write('********************************************* \n')
                previouseLines = previousTenLine[-10:]
                for previousLine in previouseLines:
                    f.write(previousLine)
                    
                f.write(line)
                
                nextTenLineCounter = 0
                for nextLine in inF:
#                    print ('iterating ' + nextLine + ' '+ str(nextTenLineCounter))
                    f.write(nextLine)
                    nextTenLineCounter = nextTenLineCounter + 1
                    if text in nextLine:
                        nextTenLineCounter = 0

                    if nextTenLineCounter % 5 == 0:
                        break

                for i in range(0, 3):
                    f.write('\n')

                previousTenLine = []
            if (lineCounter % 20 == 0):
                previousTenLine = previousTenLine[-9:]
                lineCounter = 0
            # do_something
    f.close()
    print ('DONE')

def main():
#    searchText(sys.argv[1], sys.argv[2])
    var = raw_input("search text: ")
    print ('searching ' + var)
    searchText(sys.argv[1], var)

# Here's our payoff idiom!
if __name__ == '__main__':
    main()