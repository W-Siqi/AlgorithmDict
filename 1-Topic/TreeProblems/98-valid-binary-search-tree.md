
# solution 1 BST转list
```py
class Solution(object):
    def isValidBST(self, root):
        self.seq = []
        
        def sequence(root):
            if not root: return 
            sequence(root.left)
            self.seq.append(root.val)
            sequence(root.right)
        
        sequence(root)
        seq = self.seq
        res = True
        for i in range(len(seq)):
            if i + 1 < len(seq) and seq[i] >= seq[i+1]: 
                res = False
                break
        return res
            
````