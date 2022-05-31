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
    if(root == null) return new TreeNode(val);
    let parent = new TreeNode(0);
    const findPos = (node, tar) =>{
        if(node === null){
            let newNode = new TreeNode(tar);
            if(parent.val < tar){
                parent.right = newNode;
            }else{
                parent.left = newNode;
            }
            return;
        }
        parent = node;
        if(node.val > tar){
            findPos(node.left, tar);
        }else{
            findPos(node.right, tar);
        }
    }
    findPos(root, val);
    return root;
};