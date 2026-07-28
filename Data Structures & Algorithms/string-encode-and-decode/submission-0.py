class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []

        while len(s) > 0:
            idxOfDelimiter = s.find('#')
            length = int(s[:idxOfDelimiter])
            output.append(s[idxOfDelimiter + 1: idxOfDelimiter + 1 + length])
            s = s[idxOfDelimiter + 1 + length:]
        
        return output