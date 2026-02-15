class Solution:
    # Function to merge words of iqual lenght
    def mergeAlternatelyIqualLenght(self, word1: str, word2: str) -> str:
        merged_word = ''
        for i in range(len(word1)):
            merged_word += word1[i] + word2[i]
        return merged_word

    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == len(word2):
            merged_word = self.mergeAlternatelyIqualLenght(word1, word2)
        elif len(word1) > len(word2):
            merged_word = self.mergeAlternatelyIqualLenght(word1[:len(word2)], word2) + word1[len(word2):]
        else:
            merged_word = self.mergeAlternatelyIqualLenght(word1, word2[:len(word1)]) + word2[len(word1):]
        return merged_word

if __name__ == '__main__':
     ej = Solution()
     print(ej.mergeAlternately("Hola","POPOololo"))