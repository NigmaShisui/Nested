names = [['Alice', 'Bob', 'Charlie'], #sublist 1 names[0]
         ['David', 'Eve', 'Frank'],     #sublist 2 names[1]
         ['Grace', 'Heidi', 'Ivan'],    #sublist 3 names[2]
         ['Judy', 'Ken', 'Laura']]      #sublist 4 names[3]

if "Ken" == names[3][1]: #names[3] is for sublist index niya, and then ang [1] is ang specific index ato nga arrayor kung unsa nga index si ken
    names[3].remove("Ken")
    print(names, "Ken has been removed")

else:
    print("Wla may Ken")