class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        index = len(prefix)
        
        for i in range (1, len(strs)):
            word = strs[i]
            index = min(index, len(word))
            print(index)
            
            for j in range(index):
                if prefix[j] != word[j]:
                    index = j
                    break
                    
        return prefix[: index]