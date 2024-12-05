from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)

        for word in strs:
            sorted_word = [0]*26
            for i in word:
                sorted_word[ord(i)-97] += 1
            anagram_dict[tuple(sorted_word)].append(word)
        return anagram_dict.values()
test_array = ["eat","tea","tan","ate","nat","bat"]
test = Solution()
print(test.groupAnagrams(test_array))
