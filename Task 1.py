a={"Vansh":80,"Jaynil":75,"Monil":70,"Hardik":60,"Gaurav":50}
b=input("Enter the name of student: ").capitalize()

if b in a:
    print("Marks:",a[b])
else:
    print("Student not found")
    
