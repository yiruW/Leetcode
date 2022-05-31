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
 * @param {number} val
 * @return {TreeNode}
 */
var insertIntoBST = function(root, val) {
    const findPos = (node, tar) =>{
        if(node === null){
            let newNode = new TreeNode(tar);
            return newNode;
        }
        if(node.val > tar){
            node.left = findPos(node.left, tar);
        }else if(node.val < tar){
            node.right = findPos(node.right, tar);
        }
        return node;
    }
    return findPos(root, val);
};