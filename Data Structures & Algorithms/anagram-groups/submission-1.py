class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Lists cannot be used as dictionary keys
        hash={}

        for i in strs:
           
            #for every string we will create a tuple having unicode of it
            count=[0] * 26

            for j in i:
                count[ord(j)-ord("a")] +=1

            key= tuple(count)

            if key in hash:
                hash[key].append(i)
            else:
                hash[key]=[i]

        return list(hash.values())

