lower_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0

def Encryption(input):
    i=0
    encrypted = ""
    
    for i in input:
        if i.islower() and lower_list.index(i) >= 21:
            encrypted+=i.replace(i,lower_list[lower_list.index(i)-21])
        elif i.isupper() and upper_list.index(i) >= 21:
            encrypted+=i.replace(i,upper_list[upper_list.index(i)-21]) 
        elif i.isupper() and upper_list.index(i) >= 4:
            encrypted+=i.replace(i,upper_list[upper_list.index(i)+5]) 
        elif i.isupper() and upper_list.index(i) <= 4:
            encrypted+=i.replace(i,upper_list[upper_list.index(i)+5])
        elif i.islower() and lower_list.index(i) <= 4:
            encrypted+=i.replace(i,lower_list[lower_list.index(i)+5])
        else:
            encrypted+=i.replace(i,lower_list[lower_list.index(i)+5])
    return encrypted  
    



def Decryption(input):
    i=0
    decrypted = ""
    for i in input:
        if i.islower() and lower_list.index(i) >= 21:
            decrypted+=i.replace(i,lower_list[lower_list.index(i)-5])
        elif i.isupper() and upper_list.index(i) >= 21:
            decrypted+=i.replace(i,upper_list[upper_list.index(i)-5]) 
        elif i.isupper() and upper_list.index(i) >= 4:
            decrypted+=i.replace(i,upper_list[upper_list.index(i)-5]) 
        elif i.isupper() and upper_list.index(i) <= 4:
            decrypted+=i.replace(i,upper_list[upper_list.index(i)+21])
        elif i.islower() and lower_list.index(i) <= 4:
            decrypted+=i.replace(i,lower_list[lower_list.index(i)+21])
        else:
            decrypted+=i.replace(i,lower_list[lower_list.index(i)-5])
    return decrypted

def Cipher(word):
    word_encrypted=Encryption(word)
    print(word_encrypted)
    word_decrypted=Decryption(word_encrypted)
    print(word_decrypted)
    
word=0

while word!=" ":
    word=input("Enter any word you want encrypted, or enter a space if you want to end the program: ")
    if word==" ":
        break
    Cipher(word)