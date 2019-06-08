---
layout: post
title: EASYPLAN Day 2
author: syncster31
comments: true
---
Now I'm, trying to figure out the splitting of a task, or more generally, splitting of a task segment, if ever the task has already been splitted. So I decided to create a different class for the task segment aside from the ```Task``` class.

A snippet of the implementation might be:

```python
task = Task()
task.split(task.task_segments[0], 10)
```

This will split the first task segment into two with the new task segment on the left having a duration of 10 days.

8:59pm
It's already been nine in the evening and I'm still working on the splitting of task. Hope to finish this this evening.

9:01
Oh I think I forgot, i still havent initialized one task segment in the constructor. This must be done as the starting point of task object. This has done it I think in the constructor:

```python
. . .
ts1 = TaskSegment(0, 1)
self.task_segments.append(ts1)
```
