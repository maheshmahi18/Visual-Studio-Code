class Sollution(object):
    def binarySearch(self, arr, t):
        low,high=0,len(arr)-1
        while(low<=high):
            midpos=(low+high)//2
            midval=arr[midpos]
            if midval==t:
                return midpos
            elif midval<t:
                low=midpos+1
            else:
                high=midpos-1
        return -1
        
sol=Sollution()       
ArrayList=eval(input())
Target=int(input())
ArrayList.sort()
print(ArrayList)
print(sol.binarySearch(ArrayList,Target))
