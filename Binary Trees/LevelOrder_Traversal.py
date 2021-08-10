def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def preOrder(node, level):
            if node:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(node.val)
                preOrder(node.left, level + 1)
                preOrder(node.right, level + 1)
        preOrder(root, 0) # @root is at level 0
        return res
