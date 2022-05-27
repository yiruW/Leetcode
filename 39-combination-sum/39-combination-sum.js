/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    candidates.sort((a,b) => a-b);
    const res = [];
    const comb = [];
    backTracking(0, 0);
    return res;
    
    function backTracking(sum, j){
        if(sum === target){
            res.push(Array.from(comb));
            return;
        }
        for(var i = j; i<candidates.length; i++){
            const n = candidates[i];
            if(n > target - sum) break;
            sum += n;
            comb.push(n);;
            backTracking(sum, i);
            sum -= n;
            comb.pop();
        }
    }
};
