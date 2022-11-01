class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = 0
        words = []
        start = False
        for idx,t in enumerate(text):
            if t == ' ':
                spaces += 1
                if start == True:
                    start = False
                    words.append((start_idx,idx-1))

            else:
                if start == False:
                    start = True
                    start_idx = idx
                    if idx == (len(text)-1):
                        words.append((start_idx,idx))
                elif idx == (len(text)-1):
                    words.append((start_idx,idx))
        
        if len(words) == 1:
            nr_inbetween = 0
            nr_end = spaces
        else:
            nr_inbetween = spaces // (len(words)-1)
            nr_end = spaces % (len(words)-1)
        sol = ''
        for i,word in enumerate(words):
            
            sol += text[word[0]:(word[1]+1)]
            if i < len(words)-1:
                sol += ' '*nr_inbetween
        sol += ' '*nr_end
        return sol
        
                    
            
        