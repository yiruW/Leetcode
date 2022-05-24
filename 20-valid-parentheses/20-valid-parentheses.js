/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];
    if(s.length%2 != 0){return false;}
    for(var i=0; i<s.length; i++){
        const c = s.charAt(i);
        console.log(stack, c);
        if(c === '(' || c === '{' || c === '['){
            stack.push(c);
        }else{
            const outC = stack.pop();
            if((c === ')' && outC != '(') ||(c === ']' && outC != '[') || (c === '}' && outC != '{')){
                return false;
            }
        }
    }
    if(stack.length > 0){return false;}
    return true;
};