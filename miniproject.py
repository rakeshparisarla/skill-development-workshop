student_name =['ramya','raju','ravi','vinay','abhi','hemanth','satya','surya','ramu','barath']
roll_numbers =['241','242','243','244','245','246','247','248','249','250']
roll=int(input("Enter student roll number: "))
name = input("Enter student name: ")
for i in range(0,len(roll_numbers)):
    if roll== roll_numbers[i]:
        break
    else:
        i=-1
if(i!= -1):
    print("student id found in the list")
    print(roll_numbers[i],student_name[i])
else:
    print("student id not found creating new account")
    roll_numbers.append(roll)
    student_name.append(name)
    print(roll,name)