import numpy as np
import smtplib
from email.mime.text import MIMEText
from email import utils


# partecipanti = {
#     1: ("Alessio", "alessio.lombardo@polito.it"),
#     2: ("Andrea", "andrea.querio@polito.it"),
#     3: ("Diego", "diego.fida@polito.it"),
#     4: ("Nancy", "nunzia.lauriello@polito.it"),
#     5: ("Sandro", "sandro.malusa@polito.it")
# }
GMAIL_USERNAME = "dr.f2an"
GMAIL_APP_PASSWORD = "npnjueppmswadnpd"


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
    body = "Dear {},\n\nyou have been picked as the secret santa of {}!\nRemeber that the budget to buy the gift is 10 euro and we will exchange the gifts on XX december.\n\nHappy holiday season!".format(partecipanti[randomized[i]][0], partecipanti[randomized[i-1]][0])
    recipient = [partecipanti[randomized[i]][1]]
    message = MIMEText(body)
    message["Subject"] = "Granulometria Secret Santa"
    message["To"] = partecipanti[randomized[i]][1]
    message["From"] = utils.formataddr(("Granulometria", f"{GMAIL_USERNAME}@gmail.com"))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(GMAIL_USERNAME, GMAIL_APP_PASSWORD)
       smtp_server.sendmail(message["From"], recipient, message.as_string())
    print(message)
    print("\n")
