nums = [1,2,3,1]
def containsDuplicate(self, nums):
    for i in nums:
        if nums.count(i) > 1:
            return True
            break