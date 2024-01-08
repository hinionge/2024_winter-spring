# 7.1.2024
# Playing... hoped for a cone-shell pattern


import time
import random

width = 163
length = 163


def ConeShells(line):
   for rep in range (length):
       PrintLine(line)
       time.sleep(0.23)
       line = NextLine(line)


def NextLine(line):
    lastline = line
    lastline.append(0)
    lastline.insert(0,0)
    line = []
    for cell in range(1,len(lastline)-1):
    # The rules!
       if lastline[cell-1] == 1 and lastline[cell+1] == 1 and lastline[cell] == 1:
           line.append(1)
       elif lastline[cell - 1] == 0 and lastline[cell + 1] == 0 and lastline[cell] == 0:
           line.append(1)
       else:
           line.append(0)
    return line


def SeedLine():
    line = []
    how_many = 19
    out_of = 163


    for cell in range (width):
        cell_randomizer = random.randint(1,out_of)
        if cell_randomizer <= how_many:
            line.append(1)
        else:
           line.append(0)

    return line

def PrintLine(line):
    textslab = ""
    for cell in range(len(line)):
        if line[cell] == 1:
           textslab += " "
        else:
           textslab += "•"
    print(textslab)


if __name__ == "__main__":
    ConeShells(SeedLine())
