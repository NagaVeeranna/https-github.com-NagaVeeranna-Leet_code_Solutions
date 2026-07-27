class Solution {
    public int maxValidPairSum(int[] nums, int k) {
        int n = nums.length;
        int left = nums[0],sum=0;
        for(int right =k;right<n;right++)
        {
            left = Math.max(left,nums[right-k]);
            sum = Math.max(sum,(nums[right]+left));
        }
        return sum;
    }
}