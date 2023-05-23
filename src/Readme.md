File description
================
There are three files, none of them offer easy to use parameters to parse the XML files, however, if you are a programmer you can tweak to fetch the XML tag you are interested in. 
If you need help, please raise an issue and I can get back. 

1. `parseXml.py`
This script is an example to parse just one XML file and print each tag and their associated values. You can then select the tags you are interested in to parse all other XML files. 
For example: `mytree = ET.parse('workingDir/NCT04551807.xml')` is parsed and the following three lines show the output of the script. 
nct_id ['NCT04551807']
agency ['JHSPH Center for Clinical Trials']
agency_class ['Other']

2. `fetch_only_2018.py`
This script will loop through the current working directory and its sub-directories to find XML files and query if the study is published in the year >=2018. If true, then 
it will copy those XML files to a new directory called "workingDir". 

3. `loop_parseXml.py`
The script can be parsed through each of those XML files and XML tags such as role_affiliations_details, nct_agency_details etc are parsed out. 

Please see the [Terms and Conditions](https://clinicaltrials.gov/ct2/about-site/terms-conditions).
