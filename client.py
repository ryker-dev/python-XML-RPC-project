from xmlrpc.client import Server, ServerProxy

ADDRESS = "http://localhost:3000"

proxy = ServerProxy(ADDRESS)

def print_notes():
    topic = input("Topic: ")
    notes = proxy.print_topics(topic)

    if (len(notes) > 0):
        print(f"\n-- {topic} --")
        for note in notes:
            print(f"{note[0]}: {note[1]}")
    print("\n")
        
def add_note():
    topic = input("Topic: ")
    content = input("Content: ")

    proxy.add_note(topic, content)
    pass

if __name__ == '__main__':
    while True:
        print("1) Add note")
        print("2) Print notes")
        print("0) Exit")

        action = input("Action: ")

        if (action == "0"):
            exit(0)
        elif (action == "1"):
            add_note()
        elif (action == "2"):
            print_notes()
    