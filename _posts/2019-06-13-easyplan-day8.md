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

8:27pm  
I think I just solved the recursion problem. I no longer call a method from the main frame that calls a method from gantt chart class many times that results in a recursion problem. Instead, I call the gantt chart method from inside the work breakdown structure itself by referencing the parent's gantt chart.

9:38pm  
Now, existing functions are working well without any problems, adding, deleting and editing project tasks works.

I am now implementing the splitting of a task segment. Currently unable to make it work though. Will try again tomorrow.
