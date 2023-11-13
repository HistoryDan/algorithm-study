import sys

def findNode(bst, key):
    for node in bst:
        if node[0] == key:
            return node
    return

def InOrder(bst, node):
    if node:
        key = node[0]
        left = node[1]
        right = node[2]
        if key != '.':
            InOrder(bst, findNode(bst, left))
            print(key, end='')
            InOrder(bst, findNode(bst, right))

def PreOrder(bst, node):
    if node:
        key = node[0]
        left = node[1]
        right = node[2]
        if key != '.':
            print(key, end='')
            PreOrder(bst, findNode(bst, left))
            PreOrder(bst, findNode(bst, right))

def PostOrder(bst, node):
    if node:
        key = node[0]
        left = node[1]
        right = node[2]
        if key != '.':
            PostOrder(bst, findNode(bst, left))
            PostOrder(bst, findNode(bst, right))
            print(key, end='')

n = int(sys.stdin.readline().rstrip())
bst = []

for _ in range(n):
    node = sys.stdin.readline().rstrip().split()
    bst.append(node)

PreOrder(bst, bst[0])
print()
InOrder(bst, bst[0])
print()
PostOrder(bst, bst[0])