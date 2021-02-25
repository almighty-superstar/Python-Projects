IsMale=input("If you are a male type true if not type false:")
IsTall=input("If you are tall type true if not type false:")

if IsMale=="true" and IsTall=="true":
    print("You are a male and tall!")
elif IsMale=="true" and IsTall=="false":
    print("You are a male and not tall.")
elif IsMale=="false" and IsTall=="true":
    print("You are not a male and tall. ")
else:
    print("You are not a male and not tall.")