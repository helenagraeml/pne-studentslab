from Client0 import Client

if __name__ == "__main__":
    from Client0 import Client

    PRACTICE = 2
    EXERCISE = 2

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    ip = "212.128.255.78"
    port = 8080

    c = Client(ip, port)
    print(c)