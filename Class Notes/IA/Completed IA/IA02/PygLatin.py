vowels = ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'i', 'e', 'o', 'u', 'y')
def EnglishtoPigLatin():
        s = raw_input("Please Enter a sentence to translate: ")
	sentence = s.split(" ")
	latin = ""
	for word in sentence:
		if word[0] in vowels:
			latin+= word + "way" + " "
		else:
			vowel_index = 0
			for letter in word:
				if letter not in vowels:
					vowel_index += 1
					continue
				else:
					break
			latin += word[vowel_index:] + "a" + word[:vowel_index] + "ay" + " "
	return latin[:len(latin) - 1]

def Rules(d):
    d = "Words that start with a vowel (A, E, I, O, U, Y) simply have WAY appended to the end of the word. Words that start with a consonant have all consonant letters up to the first vowel moved to the end of the word (as opposed to just the first consonant letter), and AY is appended"
    return d
    
