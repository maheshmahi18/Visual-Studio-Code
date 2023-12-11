"""

94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.
 
Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]


Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Note: Please use "None" instead of "null".
 
Solution: Done in Python

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return result

def buildTreeFromList(lst):
    if not lst:
        return None

    nodes = [None if val is None else TreeNode(val) for val in lst]
    
    root = nodes[0]
    queue = [root]
    i = 1
    
    while i < len(nodes):
        current = queue.pop(0)
        
        if nodes[i] is not None:
            current.left = nodes[i]
            queue.append(nodes[i])
        
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            current.right = nodes[i]
            queue.append(nodes[i])
        
        i += 1
    
    return root


n = eval(input())
root = buildTreeFromList(n)
sol = Solution()
result = sol.inorderTraversal(root)
print(result)