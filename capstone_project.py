import os 
import random
import tkinter
os.system("clear")

new_text = ""

#self.method
#GUI visual 
#the size of the window 
#A1, ascii? and caesar error with ' '  DEcaesar have error with symbols 
#when there's no key?

#tkinter set
root = tkinter.Tk()
root.title("Cipher Encode and Decode")

#text entry widget 
txt_before = tkinter.Entry(root, width=10)
txt_before.grid(row=0, column=2)

txt_key = tkinter.Entry(root, width=10)
txt_key.grid(row=8, column=2) 

#function definitions 
class Encode():
    def __init__(self):
        global txt_before
        self.text = txt_before.get()
        
    #1
    def gibberish(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for words in self.text:
            alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            chosen_word = random.choice(alphabet)
            new_text += words + chosen_word
        global lbl_result
        lbl_result["text"] = new_text
    
    #2
    def ascii_cipher(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for words in self.text:
            #because there's also upper case letters (what happens to numbers?)
            new_text += str(ord(words.lower())) + " "
        global lbl_result
        lbl_result["text"] = new_text
    #3
    def caesar_cipher_five(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for words in self.text:
            #because there's also upper case letters (what happens to numbers?)
            ascii_num = ord(words.lower())
            the_number = int(txt_key.get())
            shifted = ascii_num + the_number
            if shifted > 122:
                shifted = (shifted - 122) + 96
            new_text += chr(shifted)
        global lbl_result
        lbl_result["text"] = new_text
    #4
    def A1Z26(self): # *there's 1s and 10s
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for words in self.text:
            ascii_num = ord(words)
            new_text += str(ascii_num - 96) + " "
        global lbl_result
        lbl_result["text"] = new_text
    #5
    def square_and_one(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for words in self.text:
            ascii_num = ord(words)
            new_text += str(chr(ascii_num ** 2 - 1))
        global lbl_result
        lbl_result["text"] = new_text
    #6
    def v_cipher_pizza(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        #result_word
        key_index = 0
        key = txt_key.get()
        alphabet_number = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        for letter in self.text:
            if letter in alphabet_number:
                column_number = alphabet_number[letter]
                #when you went through the word pizza: pizza has to loop
                if key_index == len(key):
                    key_index = 0
                #which letter in pizza 
                row_number = alphabet_number[key[key_index]]
                #preparing for the next round in loop 
                key_index += 1
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
            else:
                result_letter = letter
            #adding to result_word
            new_text += result_letter 
        global lbl_result
        lbl_result["text"] = new_text
    #random    
    def choose_random(self):
        formula_list = [self.gibberish(), self.ascii_cipher(), self.caesar_cipher_five(), self.A1Z26(), self.v_cipher_pizza] 
        formula = random.choice(formula_list)
        return formula
    #clear
    def clear_text(self):
        self.text = ""
        global new_text
        new_text = ""
        global lbl_result
        lbl_result["text"] = ""
        txt_before.delete(0,"end")
        txt_key.delete(0,"end")
    

class Decode():
    def __init__(self):
        global txt_before
        self.text = txt_before.get()
    #1
    def decode_gibberish(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for index in range(0, len(self.text), 2):
            new_text += self.text[index]
        global lbl_result
        lbl_result["text"] = new_text
    #2
    def decode_ascii_cipher(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        split_list = self.text.split(" ")
        for number in split_list:
            new_text += str(chr(int(number))) 
        global lbl_result
        lbl_result["text"] = new_text
    #3
    def decode_caesar_cipher_five(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for letter in self.text:
            the_number = int(txt_key.get())
            ascii_num = ord(letter.lower())
            shifted = ascii_num - the_number
            if shifted < 97:
                shifted = 123 - (97 - shifted)
            new_text += chr(shifted)
        global lbl_result
        lbl_result["text"] = new_text
    #4
    def decode_A1Z26(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        split_list = self.text.split(" ")
        for number in split_list:
            ascii_num = int(number) + 96
            new_text += chr(ascii_num)
        global lbl_result
        lbl_result["text"] = new_text
        #if you include space at the end it doesn't work 
    #5
    def decode_square_and_one(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        for words in self.text:
            ascii_num = ord(words)
            new_text += chr(int((ascii_num + 1)**(1/2)))
        global lbl_result
        lbl_result["text"] = new_text
    #6
    #debug 
    def decode_v_cipher_pizza(self):
        global new_text
        new_text = ""
        global txt_before
        self.text = txt_before.get()
        key_index = 0
        key = txt_key.get()
        alphabet_number = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
        for letter in self.text:
            if letter in alphabet_number:
                encode_number = alphabet_number[letter]
                #when you went through the word pizza: pizza has to loop
                if key_index == len(key):
                    key_index = 0
                #which letter in pizza 
                row_number = alphabet_number[key[key_index]]
                #preparing for the next round in loop 
                key_index += 1
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
            else:
                result_letter = letter
            #adding to result_word
            new_text += result_letter 
        global lbl_result
        lbl_result["text"] = new_text



#class variables 
encoder = Encode()
decoder = Decode()


#GUI widgets 
#encode buttons 
btn_encode_gibberish = tkinter.Button(root, text="Gibberish", command=encoder.gibberish, width=10, bg="#97c6c9")
btn_encode_gibberish.grid(row=2, column=0)
btn_encode_ascii = tkinter.Button(root, text="ASCII", command=encoder.ascii_cipher, width=10, bg="#97c6c9")
btn_encode_ascii.grid(row=3, column=0)
btn_encode_caesar = tkinter.Button(root, text="Caesar", command=encoder.caesar_cipher_five, width=10, bg="#97c6c9")
btn_encode_caesar.grid(row=4, column=0)
btn_encode_A1Z26 = tkinter.Button(root, text="A1Z26", command=encoder.A1Z26, width=10, bg="#97c6c9")
btn_encode_A1Z26.grid(row=5, column=0)
btn_encode_square_one = tkinter.Button(root, text="Square One", command=encoder.square_and_one, width=10, bg="#97c6c9")
btn_encode_square_one.grid(row=6, column=0)
btn_encode_vigenere = tkinter.Button(root, text="Vigenere", command=encoder.v_cipher_pizza, width=10, bg="#97c6c9")
btn_encode_vigenere.grid(row=7, column=0)
btn_clear = tkinter.Button(root, text="Clear", command=encoder.clear_text, width=10, bg="#97c6c9")
btn_clear.grid(row=9, column=3)

#decode buttons 
btn_decode_gibberish = tkinter.Button(root, text="DEGibberish", command=decoder.decode_gibberish, width=10)
btn_decode_gibberish.grid(row=2, column=3)
btn_decode_ascii = tkinter.Button(root, text="DEASCII", command=decoder.decode_ascii_cipher, width=10)
btn_decode_ascii.grid(row=3, column=3)
btn_decode_caesar = tkinter.Button(root, text="DECaesar", command=decoder.decode_caesar_cipher_five, width=10)
btn_decode_caesar.grid(row=4, column=3)
btn_decode_A1Z26 = tkinter.Button(root, text="DEA1Z26", command=decoder.decode_A1Z26, width=10)
btn_decode_A1Z26.grid(row=5, column=3)
btn_decode_square_one = tkinter.Button(root, text="DESquare One", command=decoder.decode_square_and_one, width=10)
btn_decode_square_one.grid(row=6, column=3)
btn_decode_vigenere = tkinter.Button(root, text="DEVigenere", command=decoder.decode_v_cipher_pizza, width=10)
btn_decode_vigenere.grid(row=7, column=3)

#label
lbl_result = tkinter.Label(root, text="")
lbl_result.grid(row=9, column=2)

lbl_enter = tkinter.Label(root, text="Enter")
lbl_enter.grid(row=0, column=1)

lbl_encode = tkinter.Label(root, text="Encode")
lbl_encode.grid(row=1, column=0)

lbl_decode = tkinter.Label(root, text="Decode")
lbl_decode.grid(row=1, column=3)

lbl_key = tkinter.Label(root, text="Enter Key")
lbl_key.grid(row=8, column=1)

lbl_result_label = tkinter.Label(root, text="Result")
lbl_result_label.grid(row=9, column=1)


root.mainloop()


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
