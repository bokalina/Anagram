def are_anagrams(a,b):
	return ''.join(sorted(a.lower())) == ''.join(sorted(b.lower()))
	# word1 ="".join(sorted(list(a.lower())))
	# word2 ="".join(sorted(list(b.lower())))
	# if (word1 == word2):
	# 	print "words are anagram"
	# else:
	# 	print "words are not anagram"
	