print("======== Password Limit Attempt ========")

password ="pass@123"
atmpt = 0

while atmpt < 3:
    user_pass =input("Enter Ur Password : ")
    
    if user_pass == password:
        print("Log in Successfully..!💞")
        break
    else:
        print("❌ Invalid Password. Please Enter the Correct Password..!")
    atmpt +=1

if atmpt == 3:
    print("Ur Account is Block...!❌♨️...Try it again few Minute...💞💫")


