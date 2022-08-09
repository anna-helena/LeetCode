class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        temp = {}
        for i,source in enumerate(sources):
            index = indices[i]
            if (s[index:(index+len(source))] == source):
                temp[index] = i
        until = 0
        new_str = ''
        while (until < len(s)):
            if until in temp:
                i = temp[until]
                target = targets[i]
                new_str = new_str + target
                until += len(sources[i])
            else:
                new_str = new_str + s[until]
                until += 1
        return new_str
        
            
        