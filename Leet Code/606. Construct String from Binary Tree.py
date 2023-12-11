"""

606. Construct String from Binary Tree

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: root = [1,2,3,4]
Output: "1(2(4))(3)"

Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"


Example 2:

Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
 
Constraints:

The number of nodes in the tree is in the range [1, 104].
-1000 <= Node.val <= 1000


Solution: Done in Python

"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def tree2str(self, root):
    if not root:
      return ""
    res = str(root.val)
    if root.left or root.right:
      res += "(" + self.tree2str(root.left) + ")"
    if root.right:
      res += "(" + self.tree2str(root.right) + ")"
    return res

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


sol = Solution()
s = eval(input())
root = buildTreeFromList(s)
print(sol.tree2str(root))
