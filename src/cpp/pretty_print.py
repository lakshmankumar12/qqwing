#!/usr/bin/python

from __future__ import print_function

vals = {'.': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9}
#unicode_chars = [ '.' , u'\u2460', u'\u2461', u'\u2462', u'\u2463', u'\u2464', u'\u2465', u'\u2466', u'\u2467', u'\u2468']

board_str="4.176..92....4..5..9.3....7..52....39...5...6.6297.4......24.1.....9.........7..."

def print_board(board_str):
    unicode_chars = [ '.' , '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    board = [ vals[i] for i in board_str ]
    rowend="-------|-------|-------||-------|-------|-------||-------|-------|-------||"
    rowend2="=======|=======|=======||=======|=======|=======||=======|=======|=======||"

    subboard_empty_chars = [ '.' ] * 9
    subboard_present_chars = [ ' ' ] * 9
    index=0
    for row in range(9):
        line1 = u""
        line2 = u""
        line3 = u""
        for col in range(9):
            val=board[index]
            index+=1
            if val == 0:
                fill_char = '.'
            else:
                fill_char = ' '
            for subcol in range(3):
                line1 += " " + fill_char
                line3 += " " + fill_char
                if subcol == 1 and val != 0:
                    line2 += "[" + unicode_chars[val]
                elif subcol == 2 and val != 0:
                    line2 += "] "
                else:
                    line2 += " " + fill_char
            line1 += " |"
            line2 += " |"
            line3 += " |"
            if col % 3 == 2:
                line1 += "|"
                line2 += "|"
                line3 += "|"
        print (line1.encode('utf-8'))
        print (line2.encode('utf-8'))
        print (line3.encode('utf-8'))
        if row % 3 == 2:
            print(rowend2.encode('utf-8'))
        else:
            print(rowend.encode('utf-8'))


import fileinput
for line in fileinput.input():   #this one will pick stdin or if some arg(s) is/are given, it will open that as a file!
    line=line.strip()
    line=line.replace(',','')
    if line:
        print_board(line)

