#create environment for the problem
import numpy as np
import random as rd

#the considered space has a width of 90, a length of 90
length = 90
width = 90

length_of_cell = 1
number_of_area_per_row = 3
length_of_area = length/number_of_area_per_row

#the list contains the position of APs
list_of_AP = []

#initialize position of each AP.
#each AP was located at the central of each area
#the position of each AP is the constant
for i in range(9):
    list_of_AP.append((i % 3 * length_of_area + length_of_area / 2 , (i - i%3) / 3 * length_of_area + length_of_area / 2));
    # print(list_of_AP[i])

#the function calculates the distance to the nearest AP
def Distance_to_NAP(pos_of_u, list_of_AP):
    max = 0
    for x in list_of_AP:
        distance = np.sqrt((pos_of_u[0] - x[0]) * (pos_of_u[0] - x[0]) + (pos_of_u[1] - x[1]) * (pos_of_u[1] - x[1]))
        if distance > max:
            max = distance
    return max


#initialize user's postion with random value
#the position of users are the constants
list_of_U = []


#initialize by using while loop
#after initializing any user's position, check the distance from that user to the nearest AP.
#if the distance is satisfied, store it into the array list_of_U.
i = 0
while i < 10:
    area_index = i%3
    list_of_U.append((rd.uniform(area_index * length_of_area, (area_index + 1)*length_of_area), rd.uniform(area_index * length_of_area, (area_index + 1)*length_of_area)))
    if(Distance_to_NAP(pos_of_u= list_of_U[i], list_of_AP= list_of_AP) >= 1):
        print(list_of_U[i])
        i = i+1
    else:
        list_of_U.remove(list_of_U[i])
    


