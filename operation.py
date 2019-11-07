#for paths
import os

#Librairy for treating pictures
import cv2
from PIL import Image

#Here numpy generate matrix
import numpy as np

#Show, Open, Create black picture
from operation import open_picture
from operation import show_picture
from operation import blanck_picture
from operation import find_first_points
from operation import incrementation

from drawing import *
















path = "images/blanck/"

#We make the treated picture into a list.
liste_treat = os.listdir(path)

for pict in liste_treat:
    img = open_picture(path + "contour0blanck.jpg")
    copy = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x, y = find_first_points(gray)


    last = []
    suivis = []
    historic = []
    pointsy = []
    
    t = 0


    ocontinuer = True
    while ocontinuer:


                  #0     #1     #2    #3
        listex = [x+1,   x-1,   x,    x]
        listey = [y,       y,   y+1,  y-1]

        region = []

        for i in range(len(listex)):
            if gray[listex[i], listey[i]] > 200:
                region.append(i)

        if t == 0:
            region = [region[0]]
            t += 1


        region = no_bloc(last, region)

        for i in region:

            if i == 0:
                x, y = incrementation(x, y, 1, 0, copy, "")
                last = []
                last.append(i)
                suivis.append(i)
                copy[x, y] = 0, 0, 255
                break
   
            if i == 1:
                x, y = incrementation(x, y, -1, 0, copy, "")
                last = []
                last.append(i)
                suivis.append(i)
                copy[x, y] = 0, 0, 255
                break

            if i == 2:
                x, y = incrementation(x, y, 0, 1, copy, "")
                last = []
                last.append(i)
                suivis.append(i)
                copy[x, y] = 0, 0, 255
                break

            if i == 3:
                x, y = incrementation(x, y, 0, -1, copy, "")
                last = []
                last.append(i)
                suivis.append(i)
                copy[x, y] = 0, 0, 255
                break



        historic.append([x, y])

        if len(historic) > 10:
            if historic[0] == historic[-1]:
                ocontinuer = False
                #copy1 = cv2.resize(copy, (800, 800))
                #show_picture("copy1", copy1, 0, "")



    print(historic)

    print("")
    print(suivis)



    last = 0
    counter_last = 0
    schema_lign = []


    for nb, i in enumerate(suivis):

        if i == last:
            counter_last += 1

        elif i != last:
            if counter_last >= 6:
                print(counter_last)
                print(nb)
                print(suivis[nb - counter_last: nb])
                print(historic[nb - counter_last: nb])

            counter_last = 0


        last = i





    b = [[117, 165], [117, 164], [117, 163], [117, 162], [117, 161], [117, 160]]

    for i in b:
        print(i)
        copy[i[0], i[1]] = 0, 255, 0

    show_picture("copy", copy, 0, "")






































