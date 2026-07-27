class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] sortedArray = nums.clone();
        Arrays.sort(sortedArray);

        for (int i = 0; i < nums.length; ++i) {
            nums[i] = search(sortedArray, nums[i]);
        }

        return nums;
    }

    private int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while (left < right) {
            int mid = (left + right) >> 1;

            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}