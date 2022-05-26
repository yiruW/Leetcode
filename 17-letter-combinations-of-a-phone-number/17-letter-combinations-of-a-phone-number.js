/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if(!digits.length) return[];
    const phone = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"];
    const pathR=[], res=[];
    backTracking(digits, 0);
    return res;
    
    function backTracking(s,index){
        if(pathR.length === digits.length){
            res.push(pathR.join(""));
            return;
        }
        for(const c of phone[s[index]]){
            pathR.push(c);
            backTracking(s, index + 1);
            pathR.pop();
        }
    }
};