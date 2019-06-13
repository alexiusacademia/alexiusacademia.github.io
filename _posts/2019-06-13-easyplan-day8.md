---
layout: post
title: EasyPlan Day 8
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-13
permalink: 2019/06/13/easyplan-day8
---
Yesterday, I came across a problem of maximum recursion and the task segments not moving when the task start date has been changed.

The task segment bug has now been fixed by modifying the ```set_start_day``` method of ```Task``` class and recursively updating the task segment positions.

```python
def set_start_day(self, s):
    s = int(s)
    self.start_day = s

    # Adjust all start of task segments
    old_start = self.task_segments[0].start
    diff = s - old_start

    for ts in self.task_segments:
        ts.start += diff
```

I stil have to find the solution to the RecursionError even though the program is working as intended. This may cause some stack overflow in the future and nobody want that especially on low memory PCs.
