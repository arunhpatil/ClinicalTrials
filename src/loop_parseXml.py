import xml.etree.ElementTree as ET
import os 
import sys

#mytree = ET.ElementTree(file='NCT0521xxxx/NCT05217459.xml')
#mytree = ET.parse('NCT0521xxxx/NCT05217459.xml')
#mytree = ET.parse('workingDir/NCT05611229.xml')
#mytree = ET.parse('workingDir/NCT03387189.xml')
required_variables = ["nct_id","agency","agency_class","last_name","role","affiliation","phone","email","name","city","state","country","zip","study_first_posted"]
outlist = list()
temp = dict()
broad_vals = dict()
contact_vals = dict()
def walk_tree_recursive(root):
    global lname;
    #do whatever with .tags here
    for child in root:
        if child.tag == "nct_id":
            global NCTID;
            NCTID = str(child.text)
        walk_tree_recursive(child)
        if child.text != " " and child.tag != " ":
            if child.tag in required_variables:
                if child.tag == "nct_id":
                    NCTID = str(child.text)
                elif child.tag == 'last_name':
                    lname = str(child.text)
                elif child.tag == 'name':
                    global instname;
                    instname = str(child.text)
                elif child.tag == 'agency':
                    broad_vals[(NCTID, '0', 'agency')] = str(child.text) 
                elif child.tag == 'agency_class':
                    broad_vals[(NCTID, '0', 'agency_class')] = str(child.text) 
                elif child.tag == 'role' or child.tag == 'affiliation':
                    try:
                        broad_vals[(NCTID, '1', 'official', lname)].append(str(child.text))
                    except KeyError:
                        broad_vals[(NCTID, '1', 'official', lname)] = [str(child.text)]
                elif child.tag == 'phone' or child.tag == 'email':
                    try:
                        try:
                            broad_vals[(NCTID, '2', instname, lname)].append(str(child.text))
                        except NameError:
                            broad_vals[(NCTID, '2', 'overall_contact', lname)].append(str(child.text))
                    except KeyError:
                        try:
                            broad_vals[(NCTID, '2', instname, lname)] = [str(child.text)]
                        except NameError:
                            broad_vals[(NCTID, '2', 'overall_contact', lname)] = [str(child.text)]
                elif child.tag == 'city' or child.tag == 'state' or child.tag == 'country' or child.tag == 'zip':
                    try:
                        broad_vals[(NCTID, '3', instname, 'address')].append(str(child.text))
                    except KeyError:
                        broad_vals[(NCTID, '3', instname, 'address')] = [str(child.text)]



basepath = os.getcwd()
reqRange = list(range(0, 180000, 5000))
count=0
for entry in os.listdir(basepath):
    if ".xml" in entry:
        count+=1
        #print(entry)
        #mytree = ET.parse('workingDir/NCT04551807.xml')
        mytree = ET.parse(entry)
        myroot = mytree.getroot()
        lname = ""
        walk_tree_recursive(myroot)
        if count in reqRange:
            print(count)
    else:
        pass


xemail = open("email_address.txt", "a+")
xadd = open("contact_address.txt", "a+")
xagency = open("role_affiliations_details.txt", "a+")
xclass = open("nct_agency_details.txt", "a+")

for x, y in broad_vals.items():
    #xkeys = x.split(',')
    if x[1] == '2':
        yjoined = "\t".join(y)
        xemail.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t" + x[3] +"\t"+yjoined+"\n")
    elif x[1] == '3':
        #yjoined = y
        yjoined = "\t".join(y)
        #print(y)
        xadd.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t" + x[3] +"\t"+yjoined+"\n")
    elif x[1] == '1':
        yjoined = "\t".join(y)
        xagency.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t" + x[3] +"\t"+yjoined+"\n")
    elif x[1] == '0':
        yjoined = y
        xclass.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t-\t" + "\t"+yjoined+"\n")

