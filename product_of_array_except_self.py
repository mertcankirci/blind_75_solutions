nums = [1,2,3,4]
def hesapla(nums,n):
        output = []
#scan from left to i
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        #scan from right to i
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output