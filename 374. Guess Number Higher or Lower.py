class Solution:
    def guessNumber(self, n: int) -> int:
        begin=1
        end=n
        while 1:
           mid=(begin+end)//2
           g=guess(mid)

           if g==0:
               return mid
           if g==1:
                begin=mid+1
           if g==-1:
                end=mid-1

        return mid