/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    if(nums.length <= 1) return nums.length;
    let curDif = 0, preDif = 0, result = 1;
    for(let i=0; i<nums.length - 1; i++){
        curDif = nums[i+1] - nums[i];
        if((curDif > 0 && preDif <= 0)||(curDif < 0 && preDif >= 0)){
            result ++;
            preDif = curDif;
        }
    }
    return result;
};