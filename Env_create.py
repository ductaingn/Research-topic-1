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
    list_of_AP.append((i % 3 * length_of_area + length_of_area / 2 , (i - i%3) / 3 * length_of_area + length_of_area / 2))
    print(list_of_AP[i])

#the function calculates the distance to the nearest AP
def distance_to_nearest_AP(pos_of_user, list_of_AP):
    min = np.inf
    for x in list_of_AP:
        distance = np.sqrt((pos_of_user[0] - x[0]) * (pos_of_user[0] - x[0]) + (pos_of_user[1] - x[1]) * (pos_of_user[1] - x[1]))
        if distance < min:
            min = distance
    return min


#initialize user's postion with random value
#the position of users are constants
list_of_users = []

#after initializing any user's position, check the distance from that user to the nearest AP,
#if the distance is satisfied, store it into the array list_of_U.
i = 0
while i < 10:
    # sinh như này là ngẫu nhiên trên từng phần thôi, không phải ngẫu nhiên trên toàn cục không gian mẫu
    area_index = i%3
    # list_of_users.append((rd.uniform(area_index * length_of_area, (area_index + 1)*length_of_area), rd.uniform(area_index * length_of_area, (area_index + 1)*length_of_area)))
    list_of_users.append((rd.uniform(0,length),rd.uniform(0,width)))
    if(distance_to_nearest_AP(pos_of_user= list_of_users[i], list_of_AP= list_of_AP) >= 1):
        print(list_of_users[i])
        i = i+1
    else:
        list_of_users.remove(list_of_users[i])

