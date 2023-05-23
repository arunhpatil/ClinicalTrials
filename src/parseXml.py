import xml.etree.ElementTree as ET
import os 
import sys

mytree = ET.parse('workingDir/NCT04551807.xml')
myroot = mytree.getroot()
required_variables = ["nct_id","agency","agency_class","last_name","role","affiliation","phone","email","name","city","state","country","zip","study_first_posted"]
outlist = list()
temp = dict()
broad_vals = dict()
contact_vals = dict()
def walk_tree_recursive(root):
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



walk_tree_recursive(myroot)
xemail = open("email_address.txt", "w+")
xadd = open("contact_address.txt", "w+")
xagency = open("role_affiliations_details.txt", "w+")
xclass = open("nct_agency_details.txt", "w+")
for x, y in broad_vals.items():
    if x[1] == '2':
        yjoined = "\t".join(y)
        xemail.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t" + x[3] +"\t"+yjoined+"\n")
    elif x[1] == '3':
        yjoined = "\t".join(y)
        xadd.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t" + x[3] +"\t"+yjoined+"\n")
    elif x[1] == '1':
        yjoined = "\t".join(y)
        xagency.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t" + x[3] +"\t"+yjoined+"\n")
    elif x[1] == '0':
        yjoined = y
        xclass.write(x[0]+"\t"+x[1] + "\t"+ x[2]+ "\t-\t" + "\t"+yjoined+"\n")



'''
# SAMPLE OUTPUT 

nct_id ['NCT04551807']
agency ['JHSPH Center for Clinical Trials']
agency_class ['Other']
last_name ['Valerie Baker, MD', 'James Segars, MD', 'David Shade, JD', 'Alma Gonzalez', 'Ruth Lathi, MD', 'Mindy Christianson, MD', 'Bhuchitra Singh', 'Mindy Christianson, MD', 'Clinical Research Team', 'Tasha Newsome', 'Kate Devine, MD', 'Lynda Kochman', 'Wendy Vitek, MD', 'Mary Andrews', 'Gretchen Hoelscher', 'Rebecca Usadi, MD', 'Michelle Starkey-Scruggs', 'Karl Hansen, MD', 'Andrea Morley', 'Christos Coutifaris', 'Aracely Casillas', 'Kevin Doody, MD', 'Karen Merryweather', 'Ryan Heitmann, MD']
role ['Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator', 'Principal Investigator']
affiliation ['Department of Gynecology and Obstetrics, Johns Hopkins School of Medicine', 'Department of Gynecology and Obstetrics, Johns Hopkins School of Medicine']
phone ['410-955-8175', '408-688-9892', '410-583-2761', '4106142000', '301-545-1423', '301-545-1289', '585-275-0250', '704-953-4832', '405-271-9204', '215-615-4202', '817-540-1157', '304-598-3100']
email ['dshade@jhmi.edu', 'agonlez@stanford.edu', 'mchris21@jhmi.edu', 'bsingh10@jhmi.edu', 'sgfclinicalresearchteam@sgfertility.com', 'Tasha.Newsome@sgfertility.com', 'lynda_kochman@urmc.rochester.edu', 'mary.andrews@atriumhealth.org', 'gretchen.hoelscher@atriumhealth.org', 'Michelle-StarkeyScruggs@ouhsc.edu', 'Andrea.Morley@pennmedicine.upenn.edu', 'aracelyc@embryo.net', 'merrymank@wvumedicine.org']
name ['Stanford University', 'Johns Hopkins', 'Shady Grove Fertility', 'University of Rochester', 'Atrium Health', 'University of Oklahoma', 'University of Pennsylvania', 'CARE Fertility', 'West Virginia University Center for Reproductive Medicine']
city ['Sunnyvale', 'Baltimore', 'Rockville', 'Rochester', 'Charlotte', 'Oklahoma City', 'Philadelphia', 'Bedford', 'Morgantown']
state ['California', 'Maryland', 'Maryland', 'New York', 'North Carolina', 'Oklahoma', 'Pennsylvania', 'Texas', 'West Virginia']
zip ['94087', '21093', '20850', '14642', '28203', '73104', '19104', '76022', '26505']
country ['United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States', 'United States']
study_first_posted ['September 16, 2020']
'''


indent = 0
ignoreElems = ['displayNameKey', 'displayName']

def printRecur(root):
    print(root)
    """Recursively prints the tree."""
    global indent
    if root.tag in ignoreElems:
        return
    print(' '*indent + '%s: %s' % (root.tag.title(), root.attrib.get('name', root.text)))
    indent += 4
    for elem in root.getchildren():
        printRecur(elem)
    indent -= 4
