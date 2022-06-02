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
 * @return {TreeNode}
 */

// logic should be:
// right -> middle -> left

var convertBST = function(root) {
    let pre = 0;
    const traversal = (node) => {
        if(!node) return;
        traversal(node.right);
        node.val += pre;
        pre = node.val;
        traversal(node.left);
    }
    traversal(root);
    return root;
};