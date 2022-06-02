class Solution {
    private void reverse(int start, int end, int[] nums){
        for(int i=start, j=end; i<j; i++, j--){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        k %= len;
        reverse(0, len-1, nums);
        reverse(0, k-1, nums);
        reverse(k, len-1, nums);
    }
}