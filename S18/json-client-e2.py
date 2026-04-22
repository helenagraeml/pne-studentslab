import http.client
import json
import termcolor


PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)

try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

person = json.loads(data1)

print("CONTENT: ")
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
