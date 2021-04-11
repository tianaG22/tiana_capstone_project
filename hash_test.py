#initializing 
import os 
import random
os.system("clear")

#function definitions 
def gibberish(text):
    new_text = ""
    for words in text:
        new_text += words + "g"
    return new_text

def caesar_cipher(text):
    new_text = ""
    for words in text:
        #because there's also upper case letters (what happens to numbers?)
        new_text += str(ord(words.lower())) 
    return new_text

def square_and_one(text):
    pass

def A1Z26(text): # *there's 1s and 10s
    new_text = ""
    for words in text:
        ascii_num = ord(words)
        new_text += str(ascii_num - 96)
    return new_text

def v_cipher(text):
    

#formula list (about 10 formulas)
formula_list = [gibberish, caesar_cipher, square_and_one, A1Z26, v_cipher] 
     #Vigenère Cipher, binary, column cypher, 

#random index
index = random.randint(0, len(formula_list)-1)

#user input 
text = input("Enter text > ")

#result 
print(formula_list[index](text))

