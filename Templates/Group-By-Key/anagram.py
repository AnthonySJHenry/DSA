"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


Example 1:
    Input: strs = ["act","pots","tops","cat","stop","hat"]
    Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
    Input: strs = ["x"]
    Output: [["x"]]

Example 3:
    Input: strs = [""]
    Output: [[""]]

Constraints:
    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.
"""


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    newArr = []
    for w in strs:
        nestedArr = []
        w_sorted = "".join(sorted(w))
        for possible_anagram in strs:
            if w_sorted == "".join(sorted(possible_anagram)):
                nestedArr.append(possible_anagram)
        if nestedArr in newArr:
            continue
        newArr.append(nestedArr)
    return newArr


# Optimized Solution
"""
def groupAnagrams(self, strs: List[str]) ->
  List[List[str]]:
      anagrams = {}
      for word in strs:
          key = ''.join(sorted(word))  # O(k log k)
          if key not in anagrams:
              anagrams[key] = []
          anagrams[key].append(word)   # O(1) average
      return list(anagrams.values())
"""
