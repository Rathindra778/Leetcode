class Solution:
    def isBalanced(self, root):

        def height(root):
            if not root:
                return 0

            leftH = height(root.left)
            rightH = height(root.right)

            return max(leftH, rightH) + 1

        def checkBalanced(root):
            if not root:
                return True

            leftH = height(root.left)
            rightH = height(root.right)

            if abs(leftH - rightH) > 1:
                return False

            return checkBalanced(root.left) and checkBalanced(root.right)

        return checkBalanced(root)