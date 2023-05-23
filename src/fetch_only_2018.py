import xml.etree.ElementTree as ET
import os 
import sys

basepath = os.getcwd()
#entries = os.listdir(cwd)
#print(entries[0:5])
for entry in os.listdir(basepath):
    if not 'workingDir' in entry:
        if os.path.isdir(os.path.join(basepath, entry)):
            newEntry = os.listdir(os.path.join(basepath, entry))
            destination = os.path.join(basepath, 'workingDir')
            #print(destination)
            for eachentry in newEntry:
                filename = os.path.join(basepath, entry, eachentry)
                #print(filename)
                mytree = ET.parse(filename)
                myroot = mytree.getroot()
                datereq = myroot.find('study_first_posted').text.split(" ")[2]
                #print(datereq)
                if datereq >= '2018':
                    comm = "cp " + str(filename) + " " + str(destination)
                    os.system(comm)
                    #print("Arun")
                    #print(datereq)
            #print(entry)
    else:
        pass
mytree = ET.parse('NCT0561xxxx/NCT05610072.xml')
myroot = mytree.getroot()
print(myroot.find('study_first_posted').text.split(" ")[2])

'''
for x in myroot.findall('food'):
    item =x.find('item').text
    price = x.find('price').text
    print(item, price)
for x in myroot:
    print(x.tag, x.attrib)

# <study_first_posted type="Estimate">November 9, 2022</study_first_posted>
'''
