function are_anagrams(a,b){
	var word1 = a.replace(/[^A-Za-z]/, '').toLowerCase().split("").sort().join("");
	var word2 = b.replace(/[^A-Za-z]/, '').toLowerCase().split("").sort().join("");
	if (word1 == word2){
		console.log("words are anagrams");
	} else {
		console.log("words are not anagrams");
	}
}
are_anagrams(a,b);