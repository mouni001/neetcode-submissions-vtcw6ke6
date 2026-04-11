class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        new_word = ""

        for index in range(length):
            new_word = new_word + word1[index] + word2[index]
        
        if len(word1) > len(word2):
            new_word += word1[length:]
        else:
            new_word += word2[length:]
        return new_word