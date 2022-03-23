from xmlrpc.client import Server, ServerProxy

ADDRESS = "http://localhost:3000"

proxy = ServerProxy(ADDRESS)

def print_notes(topic):
    notes = proxy.print_topics(topic)

    print(f"-- {topic} --")
    for note in notes:
        print(f"{note[0]}: {note[1]}")
        
def add_note(topic, content):
    proxy.add_note(topic, content)
    pass

if __name__ == '__main__':
    ##add_note("topic1", "Test test test")
    print_notes("topic1")
    