from lxml import etree
from xml.dom import minidom

def validateXML(dtd_file, xml_file):
    dtd = etree.DTD("hw4.dtd")
    root = etree.parse("hw4.xml")
    print("XML valid = "+str(dtd.validate(root)))
    print("\n")

def printHospitalsInfo(hospitals):
    print"******************************************"
    print"Hospitals\n******************************************"
    for h in hospitals:
        print("\nHospital ID: "+h.attributes['id'].value)
        print("Hospital Name: "+h.attributes['name'].value)
        print("Hospital Location: "+h.attributes['location'].value)
        doctors = h.getElementsByTagName('Doctor')
        print("\n\tDoctors\n")
        for d in doctors:

            print("\tID\tName\tSpecialty\n")
            print("\t"+d.attributes['id'].value+"\t"+d.attributes['name'].value+"\t"+d.getElementsByTagName('specialty')[0].firstChild.nodeValue)

        print "\n"

    print"******************************************"
    print"Hospitals End\n******************************************\n"


def printPatientsInfo(patients):
    print"******************************************"
    print"Patients\n******************************************"
    for p in patients:
        print("\nPatient ID: "+p.attributes['id'].value)
        print("Date of Birth: "+p.attributes['dateOfBirth'].value)
        hospitals_attending = p.getElementsByTagName('HospitalAttending')
        print("\n\tHospitals Attending\n")
        for h in hospitals_attending:
            print("\tid\tdate_joined\n")
            print("\t"+h.attributes['id'].value+"\t"+h.attributes['dateJoined'].value+"\n")

            illnesses = h.getElementsByTagName('Illness')
            print("\n\t\tIllnesses")
            for il in illnesses:
                print("\t\t"+il.firstChild.nodeValue)
    print"******************************************"
    print"Patients End\n******************************************\n"


def parseXML(xml_file):
    xmldoc = minidom.parse(xml_file)
    hospitals = xmldoc.getElementsByTagName('Hospital')
    patients = xmldoc.getElementsByTagName('Patient')
    printHospitalsInfo(hospitals)
    printPatientsInfo(patients)


if __name__ == "__main__":
    validateXML("hw4.dtd","hw4.xml")
    parseXML("hw4.xml")
