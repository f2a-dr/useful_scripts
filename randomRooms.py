# from rdoclient import RandomOrgClient

# r = RandomOrgClient("03575034-503c-4e42-88c5-2c096197c1f4")

# people = r.generate_integer_sequences(1, 5, 1, 5, replacement=False, base=10)
# rooms = r.generate_integer_sequences(1, 2, 2, 3, replacement=False, base=10)

import numpy as np

# rng = np.random.Generator(1)
people = [1,2,3,4,5]
rooms = [2,3]
np.random.shuffle(people)
np.random.shuffle(rooms)


# print(rooms)
# print(people)


names = {
    1: "Alessio",
    2: "Andrea",
    3: "Diego",
    4: "Francesco",
    5: "Sandro"
    # "Alessio": 1,
    # "Andrea": 2,
    # "Diego": 3,
    # "Francesco": 4,
    # "Sandro": 5
}

print("#################\n")
# for i in range(len(rooms[0])):
#     print("Nella camera da {} ci saranno:".format(rooms[0][i]))
#     if i == 0:
#         for j in range(0, rooms[0][i]):
#             print(names[people[0][j]])
#     elif i != 0:
#         for j in range(rooms[0][i-1], rooms[0][i-1]+rooms[0][i]):
#             print(names[people[0][j]])
#     print("#################")

for i in range(len(rooms)):
    print("Nella camera da {} ci saranno:".format(rooms[i]))
    if i == 0:
        for j in range(0, rooms[i]):
            print(names[people[j]])
    elif i != 0:
        for j in range(rooms[i-1], rooms[i-1]+rooms[i]):
            print(names[people[j]])
    print("#################")

print("\n#################")




