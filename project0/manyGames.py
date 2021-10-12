list = ["apex legends", "counter strike global offensive", "madden", "nba 2k"]
print("I like these games")
for x in list: 
    print(x)
z = input("how many games do you want to add")
def add(amount_of_games):
    for a in range(0, int(amount_of_games)):
        y = input("what game do you want to add (one at a time)")
        list.append(y)
        for x in list:
            print(x)
add(z)
            