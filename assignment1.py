# Take college  Details as Input   
college_name = input("Enter the college name: ")                       
location = str(input("Enter college locations :"))        
courses = set(input("Enter course names separated by commas: ").split(','))
placement=input("In the college placement? (yes/no): ")
college_fees=input("Enter the college fees:")
seats_avaible=tuple(input("Enter seats available separated by commas: ").split(','))
num_students = int(input("Enter the number of students: "))           
num_faculty = int(input("Enter the number of faculty members: "))    
established_year = int(input("Enter the year of establishment: "))    
naac_grade = input("Enter the NAAC grade (e.g., A, A+, B++): ")        
is_autonomous = input("Is the college autonomous? (yes/no): ") 
college_info=  {
    "college_name" :college_name,
    "location" : location,
    "courses" : courses }

print("college_name:")
print("College Locations :", location)
print("College Courses (Set):", courses)
print("placement:")
print("college_fees:")
print("seats_avaible:", seats_avaible)
print("num_student:")
print("num_faculty:")
print("establish:")
print("naac_grade:")
print("is_autonomous")
print("coolege_info:", college_info)