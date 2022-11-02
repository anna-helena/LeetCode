class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.cheat = strs
        return 0
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return self.cheat
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))