from xmlrpc.server import SimpleXMLRPCServer
import xml.dom.minidom

IP = ("localhost", 3000)
FILENAME = "database.xml"
server = SimpleXMLRPCServer(IP, allow_none=True)

domtree = xml.dom.minidom.parse(FILENAME)
group = domtree.documentElement

class function_class:

    def add_note(self, topic, text, timestamp):
        topics = group.getElementsByTagName("topic")

        exists = False
        for topic in topics:
            if (topic.getAttribute('name') == topic):
                exists = True
                break
        
        if (exists):
            pass

    def print_topics(self):
        notes = group.getElementsByTagName("topic1")

        print(notes)
        ret = []
        for note in notes:
            print(note)
            topic_name = note.getAttribute('name')
            text = group.getElementsByTagName("text")[0].childNodes[0].childNodes[0].nodeValue
            timestamp = group.getElementsByTagName("timestamp")[0].childNodes[0].childNodes[0].nodeValue
            ret.append([topic_name, text, timestamp])

            return ret

#### Register functions
server.register_instance(function_class())
####

if __name__ == '__main__':
    try:
        print("Starting server")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server")
    