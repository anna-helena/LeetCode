from collections import defaultdict
import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #make hash from s
        s_ = defaultdict(list)
        for idx,val in enumerate(s):
            temp = s_[val]
            temp.append(idx)
            s_[val] = temp
        count = 0
        for word in words:
            last_idx = -1
            if len(word) == 0:
                count += 1
                continue
            found = True
            for w in word:
                occurences = s_[w]
                idx = bisect.bisect_right(occurences,last_idx)
                if idx > len(occurences)-1:
                    found = False
                    break
                else:
                    last_idx = occurences[idx]
            if found:
                count += 1
        return count
                    
                    