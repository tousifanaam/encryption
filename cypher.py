from random import randint
import string

def cypher(messege):
	# encryption level 1
	# dictionary storing morsecode
	morsecode_dict = {
	    "a": ".-", "b": "-...", "c": "-.-.",
	    "d": "-..", "e": ".", "f": "..-.",
	    "g": "--.", "h": "....", "i": "..",
	    "j": ".---", "k": "-.-", "l": ".-..",
	    "m": "--", "n": "-.", "o": "---",
	    "p": ".--.", "q": "--.-", "r": ".-.",
	    "s": "...", "t": "-", "u": "..-",
	    "v": "...-", "w": ".--", "x": "-..-",
	    "y": "-.--", "z": "--..","0": "-----",
	    "1": ".----", "2": "..---", "3": "...--",
	    "4": "....-", "5": ".....", "6": "-....",
	    "7": "--...", "8": "---..", "9": "----.",
	    ".": ".-.-.-", ",": "--..--", "?": "..--..",
	    "'": ".----.", "!": "-.-.--", "/": "-..-.",
	    "(": "-.--.", ")": "-.--.-", "&": ".-...",
	    ":": "---...", ";": "-.-.-.", "=": "-...-",
	    "+": ".-.-.", "-": "-....-", "_": "..--.-",
	    '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
	    "¿":"..-.-", "¡": "--...-", "start": "-.-.-",
	    "end": "...-.-",}
		
	# converting to lowercase
	# as the dictionary has no
	# uppercase character as key
	messege = messege.lower()

	# translating the messege
	# into a string encoded as morsecode
	morse_string = ''
	for i in messege:
	    if i == ' ':
	        morse_string += '/ '
	    else:
	        morse_string += morsecode_dict[i]
	        morse_string += ' '
	
	messege = morse_string # now messege is a m-c

	mym = len(messege) # mix your messege

	# encryption level 2
	x_list = list(messege)
	code = ''
	cypher_txt = ''

	length = len(messege)

	for _ in range(1, mym + 1):
		# hopper
		hopperv = randint(0, length - 1)
		code += str(hopperv)
		hopper = x_list[hopperv]
		del x_list[hopperv]

		# popper
		popperv = randint(0, length - 2)
		code += str(popperv)
		x_list.insert(popperv, hopper)


	# encryption level 3
	base_10 = [
		'0', '1', '2', '3', '4', 
		'5', '6', '7', '8', '9',]
	# v1
	v_r = randint(0, 9)
	code += str(v_r)	
	v1 = base_10[v_r]
	del base_10[v_r]

	# v2
	v_r = randint(0, 8)	
	code += str(v_r)	
	v2 = base_10[v_r]
	del base_10[v_r]

	# v2
	v_r = randint(0, 7)	
	code += str(v_r)	
	v3 = base_10[v_r]
	del base_10[v_r]

	# v3
	v_r = randint(0, 6)	
	code += str(v_r)	
	v4 = base_10[v_r]
	del base_10[v_r]


	for i in x_list:
		if i == '.':
			i = v1
		elif i == '-':
			i = v2
		elif i == '/':
			i = v3
		elif i == " ":
			i = v4
		else:
			print("\nException: ", i + "\n")
		cypher_txt += i

		# encryption level 4
	value = [v1, v2, v3, v4]
	lar = max(value)
	lar_res = ''
	for i in value:
		if i == lar:
			lar_res += str(0)
		else:
			a = int(lar) - int(i)
			lar_res += str(a)
	code += lar_res
	# creating the cypher text
	top = len(cypher_txt)
	a = ''
	for i in range(1, top+1):
	    a += str(lar)
	ran = randint(0,9)
	cypher_txt = str(lar)+str(len(a))+str(ran)

	return cypher_txt, code


def main():
	messege = input("Messege: ")
	ct , code = cypher(messege)
	filename = input("text file name: ")
	filename += "_tcypher.txt"
	with open(filename, 'w') as file:
		file.write("key: " + code + "\n")
		file.write("Messege: " + ct)
	print("Saved.")

if __name__ == "__main__":
	main()