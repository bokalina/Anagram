def are_anagrams(a,b):
	word1 ="".join(sorted(list(a.lower())))
	word2 ="".join(sorted(list(b.lower())))
	if (word1 == word2):
		print "words are anagram"
	else:
		print "words are not anagram"
	