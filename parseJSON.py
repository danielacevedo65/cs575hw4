import json

def loadJSON(fileName):
    data = json.load(open(fileName))
    return [data["SECTION"], data["STUDENT"]]

def sections(list_of_sections):
    print("LIST OF COURSES:")
    count = 0
    for i in list_of_sections:
        count += 1
        print("    Course " + str(count))
        print("\tCourse_Name: " + i["Course_name"])
        print("\tCourse_Number: " + i["Course_number"])
        print("\tQuarter: " + i["Qtr"])
        print("\tNumber: " + i["Number"])
        print("\tYear: " + i["Year"])
    return

def students(list_of_students):
    print("LIST OF STUDENT:")
    count = 0
    for i in list_of_students:
        count += 1
        print("    Student " + str(count))
        print("\tSocial Security Number: " + i["Ssn"])
        print("\tName: " + i["Name"])
        print("\tClass: " + i["Class"])
        print("\tGrade Received: " + i["Grade"])
    return

if __name__ == "__main__":
    data = loadJSON("Sections.json")
    
    list_of_sections = data[0]

    list_of_students = data[1]
    
    sections(list_of_sections)
    
    students(list_of_students)