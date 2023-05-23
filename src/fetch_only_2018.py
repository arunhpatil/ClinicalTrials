import xml.etree.ElementTree as ET
import os 
import sys

basepath = os.getcwd()

for entry in os.listdir(basepath):
    if not 'workingDir' in entry:
        if os.path.isdir(os.path.join(basepath, entry)):
            newEntry = os.listdir(os.path.join(basepath, entry))
            destination = os.path.join(basepath, 'workingDir')
            for eachentry in newEntry:
                filename = os.path.join(basepath, entry, eachentry)
                mytree = ET.parse(filename)
                myroot = mytree.getroot()
                datereq = myroot.find('study_first_posted').text.split(" ")[2]
                if datereq >= '2018':
                    comm = "cp " + str(filename) + " " + str(destination)
                    os.system(comm)
                    #print("Arun")
    else:
        pass
