## 76. Minimum Window Substring

用sliding window來框出substring，接著check substring
是否meet the condition，也就是t的每個char都包含在substring裡面。
If so, 我們在check sliding window是否是最小長度，如果是的話，我們就紀錄
sliding window的l,r index, 接著會reduce sliding window的大小，
看看是否還meet the condition，如果是就重複當前步驟，
If not， 我們就新增char到sliding window

```script
for char in s:
    # add char into sliding window
    while meet the condition:
        # check min_len of sliding window
        # if so, record the l,r index of sliding window
        # reduce sliding window
```


[Leetcode link](https://leetcode.com/problems/minimum-window-substring/)
