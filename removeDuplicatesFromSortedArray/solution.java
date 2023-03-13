class Solution {
  public int removeDuplicates(int[] nums) {
    int leftIndex = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != nums[leftIndex]) {
        leftIndex++;
        nums[leftIndex] = nums[i];
      }
    }

    return leftIndex + 1;
  }
}