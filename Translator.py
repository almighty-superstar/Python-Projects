def translate(phrase):
    translation=''
    for letter in phrase:
        if letter in "AEIOUaeiou":
              translation= translation+ 'g'
        else:
            translation=translation+letter
    print(translation)

phrase=input("Choose a word to be translated into giraffe lanuage:")
translate(phrase)
