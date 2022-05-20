class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int slow = 0, sum = 0;
        int result = Integer.MAX_VALUE;
        for(int fast = 0; fast < nums.length; fast ++){
            sum += nums[fast];
            while(sum >= target){
                result = result < fast-slow+1 ? result : fast-slow+1;
                sum -= nums[slow];
                slow ++;
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }
}