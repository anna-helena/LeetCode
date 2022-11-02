class Codec:
    def __init__(self):
        self.lens = []
        
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        for strs_ in strs:
            self.lens.append(len(strs_))
        return ''.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        sol = []
        idx = 0
        for len_ in self.lens:
            sol.append(s[idx:(idx+len_)])
            idx += len_
        self.lens = []
        return sol
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))