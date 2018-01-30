import anagram

assert True == anagram.are_anagrams('abba','baba'), 'KO'
print 'ok'

assert True == anagram.are_anagrams('Elbow', 'Below'), 'KO'
print 'ok'

assert True == anagram.are_anagrams('School Master', 'The Classroom'), 'KO'
print 'ok'

assert True == anagram.are_anagrams('abba', 'buba'), 'KO'
print 'ok'