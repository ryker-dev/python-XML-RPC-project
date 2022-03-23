from xmlrpc.server import SimpleXMLRPCServer
import xml.dom.minidom
from lxml import etree
import time

IP = ("localhost", 3000)
FILENAME = "database.xml"
server = SimpleXMLRPCServer(IP, allow_none=True)

root = etree.Element("root")

class function_class:

    def add_note(self, topic, text):
        topic = root.xpath(f"//topic[@name='{topic}']")
        base = etree.Element("group")

        etree.SubElement(topic[0], "note", attrib={
            "content": text,
            "timestamp": str(time.time())})

        etree.ElementTree(root).write(FILENAME, pretty_print=True)
    '''     note = etree.Element("note")
        content = note.Element("content")
        content.text = text
        timestamp = note.Element("timestamp")
        timestamp.text = time.time()

        note.append(content)
        note.append(timestamp) '''

    '''     if (len(topic) > 0):
            topic.append(note)
            print(topic) '''

    def print_topics(self, topic):
        notes = root.xpath(f"//topic[@name='{topic}']/note")

        ret = []
        for note in notes:
            content = note.xpath("content")[0]
            timestamp = note.xpath("timestamp")[0]
            ret.append([timestamp.text, content.text])

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
    