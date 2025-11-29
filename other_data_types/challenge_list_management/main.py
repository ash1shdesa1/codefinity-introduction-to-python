meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#main_list 
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)

#update quantity of Ham to 100, if below 100
if ("Ham" in meat[0]) and (meat[2] < 100):
    meat[2] = 100
    print ("updated quantity to", meat[2])


seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
#Add turkey to main_list
deli_dept.append(seasonal_meat)
# print(deli_dept) - check to see if Turkey was added #

#remove condiment from main_list
deli_dept.remove(condiment)

deli_dept.sort()
print("Updated Deli List:", deli_dept)