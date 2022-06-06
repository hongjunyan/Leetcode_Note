## 143. Reorder List

- Step1: Use slow, fast pointer trick to find the middle point at link
- Step2: Reverse link from middle point to last point, e.g, 1 -> 2 -> 3 -> 4
become 1 -> 2 -> None and None <- 3 <- 4
- Step3: Merge two half link

[leetcode link](https://leetcode.com/problems/reorder-list/)