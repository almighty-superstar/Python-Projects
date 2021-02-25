tries=0
secret_word="giraffe" 
guess=0
while guess!=secret_word:
    guess=input("Choose and animal in all lowercase letters:")
    tries=tries+1
    if tries==1:
        print("The animal is yellow")
    if tries==2:
        print("The animal is yellow and has spots")
    if tries==3:
        print("The animal is yellow,has spots, and has a long neck")
    
if guess==secret_word:
    print("You win!")

    
    
    
    
""" print("You are incorrect,please try again")
    tries=tries+1
    if tries==1:
        print("The animal is yellow")
    if tries==2:
        print("The animal is yellow and has spots")
    if tries==3:
       print("The animal is yellow, has spots, and has a long neck") 
 """
