alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
i=0
x=0
def Encryption(input):
    i=0
    x=0
    while i<=len(alphabet_list):
        while x <= len(input):
            if input[i] == alphabet_list[x]:
                input[i] = alphabet_list[x+5]
                x+=1
        i+=1  
    return input  
    



def Decryption(input):
    i=0
    x=0
    while i <= len(alphabet_list):
        while x <= len(input):
            if input[i] == alphabet_list[x]:
                input[i] = alphabet_list[x-5]
                x+=1
        i+=1
    return input    

encrypt = Encryption("String")
print(encrypt)
decrypt = Decryption(encrypt)
print(decrypt)
print("Hello World")