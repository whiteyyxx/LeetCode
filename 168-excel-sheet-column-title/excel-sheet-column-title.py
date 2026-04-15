class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while(columnNumber>0):
            columnNumber-=1
            n=columnNumber%26
            res=chr(n+ord('A'))+res
            columnNumber=columnNumber//26
        return res

        