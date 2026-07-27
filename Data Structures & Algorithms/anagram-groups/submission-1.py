from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())

        # hashMap = {}

        # for i, s in enumerate(strs):
        #     c1 = Counter(s)
        #     found = False
        #     for key in hashMap.keys():
        #         c2 = Counter(key)
        #         if c1 == c2:
        #             hashMap[key].append(s)
        #             found = True
        #     if not found:
        #         hashMap[s] = [s]

        # output = []

        # for key in hashMap.keys():
        #     output.append(hashMap[key])

        # return output
