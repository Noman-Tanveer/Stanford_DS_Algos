dic = dict()
revdic = dict()
global t
t = 0
global s
s = None
stack = []

def dfs(diction, node):
    stack.append(node)
    while any(stack):
         = diction[stack.pop()]
        [1] = True#show as explored
    # Find leader


with open('SCC.txt') as f:
    li = f.readlines()
    for i in li:
        if i.split()[0] in dic.keys():
            dic[i.split()[0]].append(i.split()[1])
        else:
            dic[i.split()[0]] = [i.split()[1]]

    for j in li:
        if j.split()[1] in revdic.keys():
            revdic[j.split()[1]].append(j.split()[0])
        else:
            revdic[j.split()[1]] = [j.split()[0]]

for k in dic.keys():
    dic[k] = [dic[k], False]

for l in revdic.keys():
    revdic[l] = [revdic[l], False]

for m in revdic.keys():
