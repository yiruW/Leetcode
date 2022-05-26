/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
var combinationSum3 = function(k, n) {
    if(k > 9 || k < 1) return [];
    const path = [], res = [];
    backTracking(1, 0);
    return res;
    
    function backTracking(startIndex, sum){
        if(path.length == k){
            if(sum == n) res.push(Array.from(path));
            return;
        }
        if(sum > n){return;}
        for(var i=startIndex; i<10; i++){
            sum += i;
            path.push(i);
            backTracking(i+1, sum);
            sum -= i;
            path.pop();
        }
    }
};