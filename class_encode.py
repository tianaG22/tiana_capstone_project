import os 
import random
os.system("clear")

#function definitions 
class Encode():
    def __init__(self):
        self.text = input("Enter text > ")
    
    #1
    def gibberish(self):
        new_text = ""
        for words in self.text:
            new_text += words + "g"
        return new_text
    
    #2
    def ascii_cipher(self):
        new_text = ""
        for words in self.text:
            #because there's also upper case letters (what happens to numbers?)
            new_text += str(ord(words.lower())) + " "
        return new_text
    #3
    def caesar_cipher_five(self):
        new_text = ""
        for words in self.text:
            #because there's also upper case letters (what happens to numbers?)
            ascii_num = ord(words.lower())
            shifted_five = ascii_num + 5
            if shifted_five > 122:
                shifted_five = (shifted_five - 122) + 97
            new_text += chr(shifted_five)
        return new_text
    #4
    def A1Z26(self): # *there's 1s and 10s
        new_text = ""
        for words in self.text:
            ascii_num = ord(words)
            new_text += str(ascii_num - 96) + " "
        return new_text
    #5
    def square_and_one(self):
        new_text = ""
        for words in self.text:
            ascii_num = ord(words)
            new_text += str(chr(ascii_num ** 2 - 1))
        return new_text
    #6
    def v_cipher_pizza(self):
        new_text = "" #result_word
        pizza_index = 0
        pizza = "pizza"
        alphabet_number = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        for letter in self.text:
            column_number = alphabet_number[letter]
            #when you went through the word pizza: pizza has to loop
            if pizza_index > len(pizza):
                pizza_index = 0
            #which letter in pizza 
            row_number = alphabet_number[pizza[pizza_index]]
            #preparing for the next round in loop 
            pizza_index += 1
            #adding the number of column and row 
            result_letter_number = column_number + row_number
            #number has to be less than 25=z
            if result_letter_number > 25:
                result_letter_number -= 25 
            #find the key from value
            keys = list(alphabet_number.keys())
            values = list(alphabet_number.values())
            index = values.index(result_letter_number)
            result_letter = keys[index] 
            #adding to result_word
            new_text += result_letter 
        return new_text
        
    def choose_random(self):
        formula_list = [self.gibberish(), self.ascii_cipher(), self.caesar_cipher_five(), self.A1Z26(), self.v_cipher_pizza] 
        formula = random.choice(formula_list)
        return formula
    

class Decode():
    def __init__(self):
        self.text = input("Enter text > ")
    #1
    def decode_gibberish(self):
        new_text = ""
        for index in range(0, len(self.text), 2):
            new_text += self.text[index]
        return new_text
    #2
    def decode_ascii_cipher(self):
        new_text = ""
        split_list = self.text.split(" ")
        for number in split_list:
            new_text += str(chr(int(number))) 
        return new_text
    #3
    def decode_caesar_cipher_five(self):
        new_text = ""
        for letter in self.text:
            ascii_num = ord(letter.lower())
            shifted_five = ascii_num - 5
            if shifted_five < 97:
                shifted_five = 123 - (97 - shifted_five)
            new_text += chr(shifted_five)
        return new_text
    #4
    def decode_A1Z26(self):
        new_text = ""
        split_list = self.text.split(" ")
        for number in split_list:
            ascii_num = int(number) + 96
            new_text += chr(ascii_num)
        return new_text
        #if you include space at the end it doesn't work 
    #5
    def decode_square_and_one(self):
        new_text = ""
        for words in self.text:
            ascii_num = ord(words)
            new_text += chr(int((ascii_num + 1)**(1/2)))
        return new_text
    #6
    def decode_v_copher_pizza(self):
        new_text = ""
        pizza_index = 0
        pizza = "pizza"
        alphabet_number = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        for letter in self.text:
            encode_number = alphabet_number[letter]
            #when you went through the word pizza: pizza has to loop
            if pizza_index > len(pizza):
                pizza_index = 0
            #which letter in pizza 
            row_number = alphabet_number[pizza[pizza_index]]
            #preparing for the next round in loop 
            pizza_index += 1
            #getting column number  
            column_number = encode_number - row_number
            #number has to be more than 0=a
            if column_number < 0:
                column_number += 25 
            #find the key from value
            keys = list(alphabet_number.keys())
            values = list(alphabet_number.values())
            index = values.index(column_number)
            result_letter = keys[index] 
            #adding to result_word
            new_text += result_letter 
        return new_text


#encode1 = Encode()
#print(encode1.gibberish())
#print(encode1.caesar_cipher())
#print(encode1.A1Z26())
#print(encode1.choose_random())
#print(encode1.square_and_one())
#print(encode1.decode_gibberish())
#encode.ascii_decode
#print(encode1.caesar_cipher_five())
#print(encode1.v_cipher_pizza())
#decode1 = Decode()
#print(decode1.decode_gibberish())
#print(decode1.decode_ascii_cipher())
#print(decode1.decode_caesar_cipher_five())
#print(decode1.decode_A1Z26())
#print(decode1.decode_square_and_one())
#print(decode1.decode_v_copher_pizza())
