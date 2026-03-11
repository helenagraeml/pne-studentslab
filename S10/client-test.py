from Client0 import Client

IP = "212.128.255.69"
PORT = 8080

print("To Server: Message 0")

for i in range(5):

    message = f"Message {i}"
    print(f"To Server: {message}")

    # Create client
    c = Client(IP, PORT)

    # Send message using talk()
    response = c.talk(message)

    # Print server response
    print(f"From Server: {response}")