import numpy as np


# partecipanti = {
#     1: ("Alessio", "alessio.lombardo@polito.it"),
#     2: ("Andrea", "andrea.querio@polito.it"),
#     3: ("Diego", "diego.fida@polito.it"),
#     4: ("Nancy", "nunzia.lauriello@polito.it"),
#     5: ("Sandro", "sandro.malusa@polito.it")
# }

filename = "partecipanti.csv"
partecipanti = []
counter = 1
with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        toAdd = [counter, (str(line[0]), str(line[1]))]
        partecipanti.append(toAdd)
        counter += 1

partecipanti = dict(partecipanti)

randomized = np.linspace(1, len(partecipanti), len(partecipanti))
randomized = [int(i) for i in randomized]
np.random.shuffle(randomized)

for i in range(len(randomized)):
    message = "Dear {},\\n\\nyou have been picked as the secret santa of {}!\\nRemeber that the budget to buy the gift is 10 € and we will exchange the gifts on XX december.\\nHappy holiday season!".format(partecipanti[randomized[i]][0], partecipanti[randomized[i-1]][0])
    command = "echo -en 'Subject:Granulometria Secret Santa\\n\\n{}' | ssmtp {}".format(message, partecipanti[randomized[i]][1])
    print(command)
    print("\n")
