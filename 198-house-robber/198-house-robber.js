/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let len = nums.length;
    if(len == 1){return nums[0];}
    let dp = [nums[0], Math.max(nums[0], nums[1])];
    for(let i=2; i<len; i++){
        dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
    }
    // return Math.max(dp[len-1], dp[len-2]);
    return dp[len-1];
};