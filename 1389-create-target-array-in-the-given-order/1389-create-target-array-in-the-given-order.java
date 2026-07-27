class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int length = nums.length;
        List<Integer> targetList = new ArrayList<>();
        for (int i = 0; i < length; i++)
        {
            targetList.add(index[i], nums[i]);
        }
        int[] resultArray = new int[length];
        for (int i = 0; i < length; i++) 
        {
            resultArray[i] = targetList.get(i);
        }
      
        return resultArray;
    }
}