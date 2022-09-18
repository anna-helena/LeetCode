# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    dictionary = Hash.new
    i = 0
    while i < nums.length
        return dictionary[target-nums[i]], i if dictionary[target-nums[i]]
        dictionary[nums[i]] = i

        i += 1
    end
    []  
end