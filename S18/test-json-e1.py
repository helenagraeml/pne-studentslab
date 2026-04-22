import json
import termcolor
from pathlib import Path

jsonstring = Path("people-e1.json").read_text()

person = json.loads(jsonstring)
people = person["client"]
for client in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(client["Firstname"], client["Lastname"])
    termcolor.cprint("Age: ", 'green', end="")
    print(client['age'])
    termcolor.cprint("Phone numbers: ", 'green', end='')
    phoneNumbers = client['phoneNumber']
    print(len(phoneNumbers))

    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
