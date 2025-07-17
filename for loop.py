data={
        1:{'name':'raja','exam_status':'True','python':100,'sql':98,'html':95},
        2:{'name':'sri','exam_status':'True','python':98,'sql':90,'html':85},
        3:{'name':'naveen','exam_status':'false','python':None,'sql':None,'html':None},
        4:{'name':'raju','exam_status':'True','python':50,'sql':60,'html':79},

    }
for i in data.keys():
        print(f"{i},{data[i]["name"]}")
stuid=int(input("enter the student id:"))
if stuid in data:
        if data[stuid]["exam_status"]:
                total=(data)

                