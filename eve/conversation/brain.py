import aiml
import os
import inspect
import tempfile
from pprint import pprint
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
from xml.dom import minidom



_kernel = aiml.Kernel()

def create_startfile(path):
    with open(path, 'w') as f:
        root = Element('aiml')
        tree = ElementTree(root)

        category = Element('category')
        root.append(category)

        pattern = Element('pattern')
        pattern.text = 'LOAD AIML B'
        category.append(pattern)

        template = Element('template')
        category.append(template)

        learn = Element('learn')
        learn.text = os.path.dirname(aiml.__file__) + '/standard/*.aiml'
        template.append(learn)

        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml()
        f.write(xmlstr)

def startup():
    path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    brain_path = path + "/bot_brain.brn"
    start_path = path + "/std-startup.xml"
    if os.path.isfile(brain_path):
        _kernel.bootstrap(brainFile = brain_path)
    else:
        startup(start_path)
        _kernel.bootstrap(learnFiles = start_path, commands = "load aiml b")
        _kernel.saveBrain(brain_path)

def chat(message):
    return _kernel.respond(message)


if __name__ == '__main__':
    startup()
    while True:
        message = raw_input('Enter a message: ')
        chat(message)