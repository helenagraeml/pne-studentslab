import socket
PORT = 8081
IP = "212.128.255.64"

while True:
  message = input("Enter your message: ")

  if message.lower() == "exit":
      print("Client closed.")
      break

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
      s.connect((IP, PORT))
      s.send(message.encode("utf-8"))
      print("message printed succesfully")

  except ConnectionRefusedError:
      print("Error: Could not connect to the server")
  except Exception as e:
      print("An unexpected error occured", {e})
  finally:
      s.close()

  s.close()