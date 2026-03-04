from Client0 import Client

if __name__ == "__main__":
    from Client0 import Client

    PRACTICE = 2
    EXERCISE = 1

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    # -- Parameters of the server to talk to
    ip = "212.128.255.78"  # your IP address
    port = 8080

    # -- Create a client object
    c = Client(IP, PORT)

    # -- Test the ping method
    c.ping()
