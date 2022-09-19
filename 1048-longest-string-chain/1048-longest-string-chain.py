class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #order words by size
        #initialize empty array for each word size
        #write fct to determine if predecessor or not
        #have dic that saves longest until that var
        
        def is_predecessor(word, word_prev):
            for i in range(0,len(word)):
                if ((word[:i] + word[(i+1):]) == word_prev):
                    return True
            return False
                
        longest_ = [1]*len(words)
        word_len = {}
        for i,word in enumerate(words):
            temp = len(word)
            if temp in word_len:
                temp_list = word_len[temp]
                temp_list.append(i)
                word_len[temp] = temp_list
            else:
                word_len[temp] = [i]
        
        result = 1
        for length in range(min(word_len),max(word_len)+1):
            if (length-1) in word_len:
                temp_word_list_prev = word_len[length-1]
            else:
                continue
            temp_word_list = word_len[length]
            #check each word and see if there is previous word
            for temp_word in temp_word_list:
                max_len = 1
                for temp_word_prev in temp_word_list_prev:
                    if is_predecessor(words[temp_word], words[temp_word_prev]):
                        max_len = max(max_len,longest_[temp_word_prev]+1)
                longest_[temp_word] = max_len
                result = max(result,max_len)
        return result
        