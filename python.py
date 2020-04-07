#--------------------------------------------------------SETTING UP BOARD----------------------------------------------------------
from random import randint
import os
import time
# boat1["1"] = "false"
# boat2["1"] = "false"
# boat1[number] = "false"
# boat2[number] = "false"
repeat1 = "false"
repeat2 = "false"
repeat3 = "false"
repeat4 = "false"
board = {"2":[],"1":[]}
boat1 = {"2":"","1":""}
boat2 = {"2":"","1":""}
row1 = {"2":"","1":""}
col1 = {"2":"","1":""}
row2 = {"2":"","1":""}
col2 = {"2":"","1":""}
def clear():
    os.system('cls')
for x in range(4):
  board["1"].append(["O"] * 4)
for x in range(4):
  board["2"].append(["O"] * 4)

def print_board(board):
  for row in board:
    print "  ".join(row)
#----------------------------------------------PLR 1 SET---------------------------------------------------------------------

#ship 1--------------------------------------------------------------------------------------------------------------------------
# while row1["1"] not in range(1,9) or col1["1"] not in range(1,9):
#   clear()
#   if repeat2 == "true":
#     if isinstance(row1["1"], int) == False or isinstance(col1["1"], int) == False:
#       print("Please only type integers")
#       print("------------------------------------------------------")
#     elif row1["1"] not in range(1,9) or col1["1"] not in range(1,9):
#       print("Please only type coordinates between 1-8")
#       print("------------------------------------------------------")
#     else:
#       break
#   row1["1"] = raw_input("Player 1, set your row coordinant for ship number 1(x coordinant)")
#   try:
#     row1["1"] = int(row1["1"])
#   except:
#     row1["1"] = "Not a number"
#   col1["1"] = raw_input("Player 1, set your column coordinant for ship number 1(y coordinant)")
#   try:
#     col1["1"] = int(col1["1"])
#   except:
#     col1["1"] = "Not a number"
#   repeat1 = "true"
# clear()

#ship 2 -----------------------------------------------------------------------------------------------------------------------------
# while row2["1"] not in range(1,9) or col2["1"] not in range(1,9):
#   clear()
#   if repeat2 == "true":
#     if isinstance(row2["1"], int) == False or isinstance(col2["1"], int) == False:
#       print("Please only type integers")
#       print("------------------------------------------------------")
#     elif row2["1"] not in range(1,9) or col2["1"] not in range(1,9):
#       print("Please only type coordinates between 1-8")
#       print("------------------------------------------------------")
#     else:
#       break
#   row2["1"] = raw_input("Player 1, set your row coordinant for ship number 2(x coordinant)")
#   try:
#     row2["1"] = int(row2["1"])
#   except:
#     row2["1"] = "Not a number"
#   col2["1"] = raw_input("Player 1, set your column coordinant for ship number 2(y coordinant)")
#   try:
#     col2["1"] = int(col2["1"])
#   except:
#     col2["1"] = "Not a number"
#   repeat1 = "true"
# clear()





#---------------------------------------------------PLR 2 SET-------------------------------------------------------------------

#---------------------------------------------------SHIP ONE--------------------------------------------------------------------
def handle_ship(number):
  repeat2= "false"
  while row1[number] not in range(1,5) or col1[number] not in range(1,5):
    clear()
    if repeat2 == "true":
      if isinstance(row1[number], int) == False or isinstance(col1[number], int) == False:
        print("Please only type integers")
        print("------------------------------------------------------")
      elif row1[number] not in range(1,5) or col1[number] not in range(1,5):
        print("Please only type coordinates between 1-4")
        print("------------------------------------------------------")
      else:
        break
    row1[number] = raw_input("Player " + number +  ", set your row coordinant for ship number one(x coordinant)")
    try:
      row1[number] = int(row1[number])
    except:
      row1[number] = "Not a number"
      print("not number 1 row")
    col1[number] = raw_input("Player " + number + ", set your column coordinant for ship number one(y coordinant)")
    try:
      col1[number] = int(col1[number])
    except:
      col1[number] = "Not a number"
      print("not a number 1 col")
    repeat2 = "true"
    clear()
  #-----------------------------------------------SHIP TWO----------------------------------------------------------------------
  repeat2 = "false"
  while row2[number] not in range(1,5) or col2[number] not in range(1,5):
    clear()
    if repeat2 == "true":
      if isinstance(row2[number], int) == False or isinstance(col2[number], int) == False:
        print("Please only type integers")
        print("------------------------------------------------------")
      elif row2[number] not in range(1,5) or col2[number] not in range(1,5):
        print("Please only type coordinates between 1-4")
        print("------------------------------------------------------")
      else:
        break
    row2[number] = raw_input("Player " + number + ", set your row coordinant for ship number two(x coordinant)")
    try:
      row2[number] = int(row2[number])
      print("not a number 2 row")
    except:
      row2[number] = "Not a number"
    col2[number] = raw_input("Player " + number + ", set your column coordinant for ship number two(y coordinant)")
    try:
      col2[number] = int(col2[number])
      print("not a number 2 col")
    except:
      col2[number] = "Not a number"
    repeat2 = "true"
  clear()

handle_ship("1")
handle_ship("2")
row1["1"] -= 1
col1["1"] -= 1
row2["1"] -= 1
col2["1"] -= 1
row1["2"] -= 1
col1["2"] -= 1
row2["2"] -= 1
col2["2"] -= 1
while True:
  clear()
  print("Player 1, your turn.")
  print_board(board["1"])
  guess_row = int(input("Guess Row: ")) - 1
  guess_col = int(input("Guess Col: "))  - 1
  if guess_row == row1["2"] and guess_col == col1["2"] or guess_row == row2["2"] and guess_row == col2["2"]:
    clear()
    board["1"][guess_row][guess_col] = 'S'
    print_board(board["1"])
    print "You hit my battleboat!"
    if guess_row == row1["2"] and guess_col == col1["2"]:
      boat1["2"] = "Hit"
    if guess_row == row2["2"] and guess_col == col2["2"]:
      boat2["2"] = "Hit"
    if boat1["2"] == "Hit" and boat2["2"] == "Hit":
      clear()
      print_board(board["1"])
      print "PLAYER 1 WINS!"
      break
    elif guess_row not in range(8) or guess_col not in range(8):
      print "That didn't even land in the ocean."
      if (board["1"][guess_row][guess_col] == "X"):
        print "You guessed that one already."
    elif guess_row != row1["2"] or guess_row != row2["2"] or guess_col != col1["2"] or guess_col != col2["2"]:
        print "You missed my battleboat!"
        board["1"][guess_row][guess_col] = "X"

  clear()
  print("Player 2, your turn.")
  print_board(board["2"])
  guess_row = int(input("Guess Row: ")) - 1
  guess_col = int(input("Guess Col: ")) - 1
  if guess_row == row1["1"] and guess_col == col1["1"] or guess_row == row2["1"] and guess_row == col2["1"]:
    clear()
    board["2"][guess_row][guess_col] = 'S'
    print_board(board["2"])
    print "You hit my battleboat!"
    if guess_row == row1["1"] and guess_col == col1["1"]:
      boat1["1"] = "Hit"
    if guess_row == row2["1"] and guess_col == col2["1"]:
      boat2["1"] = "Hit"
    if boat1["1"] == "Hit" and boat2["1"] == "Hit":
      clear()
      print_board(board["2"])
      print "PLAYER 2 WINS!"
      break
    else:
      print board["2"][row1["1"]][col1["1"]], board["2"][row2["1"]][col2["1"]]
  else:
    if guess_row not in range(8) or guess_col not in range(8):
      print "That shot didn't even land in the ocean."
    elif(board["2"][guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleboat!"
      board["2"][guess_row][guess_col] = "X"
