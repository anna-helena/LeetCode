class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        temp = {}
        for i,source in enumerate(sources):
            index = indices[i]
            if (s[index:(index+len(source))] == source):
                temp[index] = i
        print(temp)
        until = 0
        new_str = ''
        while (until < len(s)):
            if until in temp:
                print('until', until)
                i = temp[until]
                target = targets[i]
                new_str = new_str + target
                until += len(sources[i])
                print(new_str)
            else:
                print('until2', until)
                new_str = new_str + s[until]
                until += 1
                print(new_str)
        return new_str
        
            
        