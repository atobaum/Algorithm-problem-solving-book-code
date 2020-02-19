# p689
# 20200219
# 때려침.

longest = 0

class TreeNode:
    def __init__(self):
        self.children = []
    def depth(self):
        if len(self.children):
            heights = sorted(map(lambda n: n.depth(), self.children), reverse=True)

            if len(heights) > 1:
                longest = max(longest, heights[0] + heights[1] + 2)
            return heights[0] + 1 
        return 0

def makeTree(walls):


# root를 지나는 최대 패스 길이, l: 최대 길이.
def longestLeafToLeafPath(root: TreeNode, l: int):
    if root.children.length < 2:
        return 0
    t = sorted(map(lambda n: n.depth(), root.children), reverse=True)
    return t[0] + t[1] + 2

def FORTRESS(walls):
    tree: TreeNode = makeTree(walls)
    return max(tree.depth(), longest)


print(FORTRESS([[5,5,15], [5,5,10], [5,5,5]]), " = 2")
print(FORTRESS([[21,15,20], [15,15,10], [13,12,5], [12,12,3], [19,19,2], [30,24,5], [32,10,7], [32,9,4]), " = 5")