from Client0 import Client

if __name__ == "__main__":

    PRACTICE = 2
    EXERCISE = 1

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "127.0.0.1"
    port = 8080
    c = Client(ip, port)
    c.ping()
