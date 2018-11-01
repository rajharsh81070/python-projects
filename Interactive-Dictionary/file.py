"""This is a Interactive-Dictionary build using python.
	In this i have imported two libraries.
	first one is json which i have used for handling data and the second one is difflib which is used to tell the similarity between two
	words. 
"""



import json
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def wordMeaning(word):  
	word = word.lower()
	if word.capitalize() in data: #We can either use word.title() to capitalize it.
		return data[word.capitalize()]
	elif word.upper() in data:
		return data[word.upper()]
	elif word in data:
		return data[word]
	elif len(get_close_matches(word, data.keys())) > 0:
		check = input("Did you mean '%s' instead ? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
		if check == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif check == "N":
			return "Oops! The word doesn't exists. Please double check it."
		else:
			return "We don't understand your input."
	else:
		return "Oops! The word doesn't exists. Please double check it." 

word = input("Enter Word : ")

output = wordMeaning(word)

if type(output) == list:
	for item in output:
		print(item, end='\n')
else:
	print(output)