/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    const len = nums.length;
    if(len < 4) return [];
    nums.sort((a, b) => a-b);
    const res = [];
    for(var i=0; i< len-3; i++){
        if(i>0 && nums[i] === nums[i-1]) continue;
        for(var j=i+1; j<len-2; j++){
            if(j>i+1 && nums[j] === nums[j-1]) continue;
            let a = j+1, b = len-1;
            while(a<b){
                const sum = nums[i] + nums[j] + nums[a] + nums[b];
                if(sum > target){b--; continue;}
                if(sum < target){a++; continue;}
                res.push([nums[i], nums[j], nums[a],nums[b]]);
                while(a<b && nums[a] === nums[++a]);
                while(a<b && nums[b] === nums[--b]);
            }
        }
    }
    return res;
};