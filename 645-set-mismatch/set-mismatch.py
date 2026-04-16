class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        dup=-1
        miss=-1
        for i in range(1,len(nums)+1):
            if i in d and d[i]==2:
                dup=i
            if i not in d:
                miss=i
        return [dup,miss]