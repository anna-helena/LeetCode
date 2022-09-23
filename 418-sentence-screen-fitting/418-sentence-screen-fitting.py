class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        r = 1
        c = 0
        w_idx = 0
        counter = 0
        jumping = {}
        
        def get_last_indices(r_start, c):
            w_idx = 0
            r = r_start
            counter = 0
            while True:
                word = sentence[w_idx]
                if len(word) > cols:
                    return (False,False,counter)
                temp = c + len(word)
                if (temp <= cols):
                    c = temp + (0 if (temp == cols) else 1)
                elif(temp > cols):
                    c = len(word) + (0 if (len(word) == cols) else 1)
                    r = r + 1
                if r > rows:
                    return (False,False,counter)
                if w_idx == (len(sentence)-1):
                    counter += 1
                    if r == r_start:
                        w_idx = 0
                        continue
                    return (r-r_start,c, counter)
                w_idx += 1
        
        max_word = 0
        for word in sentence:
            max_word = max(len(word),max_word)
        if max_word > cols:
            return 0
        while True:
            if c in jumping:
                (r_jump, c, count) = jumping[c]
                r += r_jump
            else:
                (r_jump, c_new, count) = get_last_indices(r, c)
                if r_jump == False:
                    return counter+count
                jumping[c] = (r_jump, c_new, count)
                c = c_new
                r += r_jump
            if r > rows:
                return counter+count-1
            counter += count
 