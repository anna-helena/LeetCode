# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        prev = {}
        import random
        mylist = [*range(0,len(wordlist))]
        random.shuffle(mylist)
        prev[mylist[0]] = master.guess(wordlist[mylist[0]])
        nr_g = 1
        if prev[mylist[0]] == 6:
            return
        idx = 1
        while (idx < len(wordlist)): 
            new_word = wordlist[mylist[idx]]
            possible = True
            for p in prev.keys():
                nr = self.count_chars(wordlist[p],new_word)
                if nr != prev[p]:
                    possible = False
                    break
            if not possible:
                idx += 1
                continue
            else:
                prev[mylist[idx]] = master.guess(new_word)
                nr_g += 1
                if prev[mylist[idx]] == 6:
                    return
                idx += 1
    
    def count_chars(self,word1,word2):
        count = 0
        for i in range(0,6):
            if word1[i] == word2[i]:
                count += 1
        return count
                