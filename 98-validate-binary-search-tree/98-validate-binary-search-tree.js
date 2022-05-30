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
 * @return {boolean}
 */

var isValidBST = function(root) {
    let pre = null;
    const getLength = (root) => {
        if(root == null) return true;
        let left = getLength(root.left);
        if(pre != null && pre.val >= root.val){
            return false;
        }
        pre = root;
        let right = getLength(root.right);
        return left && right;
    }
    return getLength(root);
};