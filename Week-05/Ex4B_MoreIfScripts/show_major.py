major_info = {'BIOL': ('Biology','Sciend Bldg, Room 310'),
             'CSCI': ('Computer Science','Sheppard Hall, Room 314'),
             'ENG' : ('English','Kerr Hall, Room 201'),
             'HIST': ('History', 'Kerr Hall, Room 114'),
             'MKT' : ('Marketing', 'Westly Hall, Room 310')}
# major code, name of major, and dept office

student_name = input("Type in First and Last name: ")
student_major_code = input("Please enter your major code: ")
major_name = ['biology', 'computer science', 'English', 'history', 'marketing']
office = ['Room 310', 'Room 314', 'Room 201', 'Room 114', 'Room 310']

if student_major_code in major_info: 
     major_name,office = major_info[student_major_code]

print(f'Hello {student_name}, your major is {major_name}, your department is {office}')

       

