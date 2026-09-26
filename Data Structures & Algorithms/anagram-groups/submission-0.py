class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = tuple(sorted(word))
            map[key] = map.get(key, []) + [word]
        return [li for li in map.values()]
