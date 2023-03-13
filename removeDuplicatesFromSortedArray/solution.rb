# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
    return 0 if nums.empty?
    i = 0
    nums.each do |num|
        if nums[i] != num
            i += 1
            nums[i] = num
        end
    end
    i + 1
    
end

# takeaways
# 1. use i to keep track of the index of the last unique element
# 2. use each to iterate through the array
# 3. use i + 1 to return the length of the array
