print("==========Check Your Garde =========")

marks=input("Enter Your Marks to get Grade: ")

if marks=="A":
    print("The Student is absent")
elif marks>= str(90):
    print("Grade: A")
elif marks >= str(70) and marks <str(90):
    print("Grade: B")
elif marks >=str(50) and marks <str(70):
    print("Grade: C")
elif marks < str(50):
    print("Grade: D")
    print("Student was Failed")
else:
    print("Invalid Grade, Please Valid Marks ")

print("======== THANKS U USING CHECK GRADE PROGRAMMMING") 