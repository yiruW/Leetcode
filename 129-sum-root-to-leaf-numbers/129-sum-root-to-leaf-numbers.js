/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
let totalSum = 0;

var sumNumbers = function(root) {
    totalSum = 0;
    goThroughNode(root, 0);
    return totalSum;
};

var goThroughNode = function(node, sum){
    if(node != null){
        sum = sum * 10 + node.val;
        if(node.left == null && node.right == null){
            totalSum += sum;
        }
        goThroughNode(node.left, sum);
        goThroughNode(node.right, sum);
    }
}