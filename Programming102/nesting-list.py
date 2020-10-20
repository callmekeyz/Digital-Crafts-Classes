people = [["Keyz","jordan",32],
    ["rick","francis",34]
    ]
print(people[0]) 
print(people[0][0]) 

  #assigning result of expression to variable
age = print(people[1][2])

  #You can modify the array in place the same way
people[0][2] = 33 
del people[1][2]
print(people)


people = [
    ["Clint","Fleetwood", 38], 
    ["Anna", "Fleetwood", 37],
    ["Peter", "Hollens", 34],
    ["Lindsey", "Sterling", 35]
]

for person in people:
    print("First, Last, Age")
    for attribute in person:
        print(attribute)

coordinates = [[10,10], [20,10],[10,20]]

for cord in coordinates:
    idx = 0
    print("Position:")
    for position in cord:
        p = "X"
        if idx == 1:
            p = "Y"
        print(f"{p}-{position}")
        idx += 1