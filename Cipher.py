# https://www.w3schools.com/python/ref_string_index.asp
# How I found the index function to find the position of an item in a list

# Initialize a list that contains the letters of the alphabet for both lower and uppercase letters
lower_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0


# define the encryption function
def Encryption(input):
    i=0
    encrypted = ""
    # checks each character in the phrase
    for i in input:
        # these conditionals find that character 5 characters over as if the list was continuous and looped over itself, as if in the 
        # list the letter a came after z, so that when certain letters were in input the shift would not go outside the range of the list  
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
    # allows outside functions to access the variables in this function, in this case, encrypted
    return encrypted  
    


# define the decryption function 
def Decryption(input):
    i=0
    decrypted = ""
    # checks each character in the phrase
    for i in input:
    # this does similar to the conditionals above only that it shifts the encrypted character over 26 minus the amount of times in the 
    # if else statement above so that the decrypted character is the same as the original character inputted 
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
    # allows outside functions to access the variables in this function, in this case, decrypted
    return decrypted


#defines the Cipher function, which controls the encrypt and decrypt functions
def Cipher(word):
    # sets encrypted input equal to a variable
    word_encrypted=Encryption(word)
    # shows the encrypted version of the original word
    print(word_encrypted)
    # decrypts the encrypted word to a variable
    word_decrypted=Decryption(word_encrypted)
    # shows the decrypted word
    print(word_decrypted)
    

word=0

# keeps running the Cipher function while the user input is not a space
while word!=" ":
    # user input to be encrypted and decrypted
    word=input("Enter any word you want encrypted, or enter a single space if you want to end the program: ")
    # stopes the loop if the input is a space
    if word==" ":
        break
    # keeps asking for a correct input if the user inputs a word or special characters
    while word is word.isalpha():
        word=input("Please enter alpahbetical characters: ")
    # runs the cipher function and encrypts and decrypts the word
    Cipher(word)