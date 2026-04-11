class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        # new_word = ""
        # O(n) if i use concatenation for words, better use a list###

        # for index in range(length):
        #     new_word = new_word + word1[index] + word2[index] # O(n)
        
        # if len(word1) > len(word2):
        #     new_word += word1[length:]
        # else:
        #     new_word += word2[length:]
        # return new_word
        parts = []

        for index in range(length):
            parts.append(word1[index])
            parts.append(word2[index])

        if len(word1) > len(word2):
            parts.append(word1[length:])
        else:
            parts.append(word2[length:])

        return "".join(parts)