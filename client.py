from xmlrpc.client import Server, ServerProxy

ADDRESS = "http://localhost:3000"

proxy = ServerProxy(ADDRESS)

def print_topics():
    topics = proxy.print_topics()

    for topic in topics:
        print(f"-- {topic[0]} --")
        print(topic[2])
        print(topic[1] + "\n")
        
def add_topic():
    pass

if __name__ == '__main__':
    print_topics()
    