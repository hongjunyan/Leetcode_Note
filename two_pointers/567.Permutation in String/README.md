## 567.Permutation in String

這題可以用sliding window來解，而sliding window等同於s1的長度，
接著iterate s2 from idx of len(s1) to idx of len(s2), 
每一次iter，都add char at right of window, and remove char 
at left of window，接著判斷window是否是s1的permutation。

```script
l = 0
for r in range(len(s1), len(s2)):
    window add s[s2]
    window remove s[s1]
    if window == s1_hashmap:
        return True
    l += 1
return False
```


[Leetcode link](https://leetcode.com/problems/minimum-window-substring/)
