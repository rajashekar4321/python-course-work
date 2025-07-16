#1
name=("raja")
for ch in name:
    print(f"ch = {ch}")

#2
name = ('raja','shekar','sri')
for ch in name:
    print(f"ch = {ch}")
        
#3
name = {1:'raja',2:'shekar',3:'sri'}
for i  in name.keys():
    print(f"{i}-(name[i].title() = {ch}")
    
#4
for i in range (1,21):
    print(f'17*{i}= {17*i}')

#5
email,pwd='raja@gmail.com','abc@12'
max_attempt=5
cur_attempt=0
while cur_attempt  <max_attempt:
    e=input("enter the email:")
    p=input("enter the password:")
    if e==email and p==pwd :
        print("login sucessfull")
        break
    else:
        print("invalid email or pwd.try again!!")
    cur_attempt+=1
else:
    print("max attempt are done.try after 5 mins")
    


               