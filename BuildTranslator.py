'''transalor 
game'''
def translate(texts):
    translation=""
    for letter in texts:
        #converting letter to lower case
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return  translation


print(translate("On"))