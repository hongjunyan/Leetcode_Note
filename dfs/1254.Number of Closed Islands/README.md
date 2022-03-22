## 1254.Number of Closed Islands

- Method1: dfs, 先將包含邊界的islands，全部填成1，再計算總共有幾個islands(leetcode 200)，就結束了。
- Mehtod2: dfs with condition, 使用leetcode 200的解法(只比leetcode 200多了2行程式)，但多了條件判斷，即如果當前的land有包含邊界，就判斷不是closed island。
- Method3: bfs with condition 

[Leetcode link](https://leetcode.com/problems/number-of-closed-islands/)
