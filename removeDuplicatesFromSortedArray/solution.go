package solution

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	// two index method, one increments linearly across the array,
	// the other only increments when a new value is found
	i := 0
	for j := 1; j < len(nums); j++ {
		if nums[j] != nums[i] {
			i++
			// shift the unique value to the front of the array
			nums[i] = nums[j]
		}
	}
	return i + 1
}
