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
var maxDepth = function(root) {
    const getDepth = (node, depth) => {
        if(node == null) return depth;
        let left = getDepth(node.left, depth + 1);
        let right = getDepth(node.right, depth + 1);
        return Math.max(left, right);
    }
    return getDepth(root, 0);
};