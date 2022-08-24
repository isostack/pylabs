def longestWord(str): 
    longest_word = max(str.split(), key = len)
    return longest_word

def longestWords(str):
    longest_word = max(str.split(), key = len)
    words = [item for item in str.split() if len(item) == len(longest_word)]
    return words
    
print(longestWord("The campers and the jumpers are here"))
print(longestWords("The campers and the jumpers are here"))