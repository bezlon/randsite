from googlesearch import search
import random

def get_site():
	words_file = open("words.txt", "r")
	words = words_file.readlines()
	new_words = []
	sites = []

	for word in words:
		new_words.append(word.strip("\n"))

	rand_word = new_words[random.randint(0, len(new_words)-1)] # Get a random word

	for site in search(rand_word, stop=random.randint(1, 69)):
		sites.append(site)

	return sites[random.randint(0, len(sites)-1)] # Finally return random site

print(get_site())