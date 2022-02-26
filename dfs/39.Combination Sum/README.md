## 39.Combination Sum.py

### Method1. DFS - binary tree
```
[2,3,4,7], target = 7
            []
        [2]     [], i + 1
   [2,2]   [2], i + 1
  
```

### Method2, DFS - general tree
再加入新的element時，i要大於等於當前index, i.e.,
for i in range(idx, len(candidates))
    cur_list.append(candidates[i])
```
                            []
    [2], idx=0   [3], idx=1    [4], idx=2    [7], idx=3
```

[Leetcode link](https://leetcode.com/problems/combination-sum/)
