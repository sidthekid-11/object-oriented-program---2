class pairelements:

    def twonum(self,nums,target):
        lookup = {}

        for i,num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target-num],i)
            lookup[num] = i

value = int(input("Enter the sum of which you want to search for: "))
print("index1=%d,index2=%d" % pairelements().twonum((1,2,3,4,5,6,7,8,9),value))


