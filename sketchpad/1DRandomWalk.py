# 7.1.2024
# Bored on a Sunday night. 1-dimensional random walk (printed line by line)


import random
import time


def RandomWalk(char,lines):
   place = 37
   for rep in range(lines):
       movement = random.randint(0,1)
       movement *= 2
       movement -= 1
       place += movement
       OutputLine(char,place)
       time.sleep(0.25)




def OutputLine(char,place):
   if place < 0:
       place = 0
   out = char
   out = char.rjust(place," ")
   print(out)






if __name__ == "__main__":
   char = "*"
   lines = 456
   RandomWalk(char,lines)
