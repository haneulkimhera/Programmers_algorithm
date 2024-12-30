from collections import defaultdict

n = int(input())
tree = dict()
parents = list(map(int,input().split()))
del_node = int(input())

for i in range(n):
    tree[i] = []

for i in range(n):
    child = i
    parent = parents[i]
    root = None
    if parent==-1:
        root = child
    else:
        tree[parent].append(child)

def cut_tree(node):
    for i in range(n):
        if node in tree[i]:
            tree[i].remove(node)
            break
    stack = [node]
    while(stack):
        curr = stack.pop()
        while(tree[curr]):
            stack.append(tree[curr].pop())
        del tree[curr]

cut_tree(del_node)

def count_tree():
    cnt = 0
    for node in tree:
        if not tree[node]:
            cnt += 1
    return cnt

cnt = count_tree()
print(cnt)