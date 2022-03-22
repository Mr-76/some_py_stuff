# coding=UTF-8
#Author Mr-76

def gimme(array):
    for index in range(len(array)):
        if (index == 0):
            maxx = array[0]
            middle = array[0]
            minim = array[0]
            maxxindex = 0
            minim_index = 0
            continue
        
        if (array[index] > maxx):
            maxx = array[index]
            maxxindex = index
            continue

        if (array[index] < minim):
            minim = array[index]
            minim_index = index
      

    for index in range(len(array)):
        if (index == maxxindex) or (index == minim_index):
            continue
        else:
            return index


