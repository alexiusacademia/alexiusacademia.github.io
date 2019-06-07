---
layout: post
title: EASYPLAN Day 2
author: syncster31
---
Now I'm, trying to figure out the splitting of a task, or more generally, splitting of a task segment, if ever the task has already been splitted. So I decided to create a different class for the task segment aside from the ```Task``` class.

A snippet of the implementation might be:
```python
task = Task()
task.split(task.task_segments[0], 10)
```
This will split the first task segment into two with the new task segment on the left having a duration of 10 days.

It's already been nine in the evening and I'm still working on the splitting of task. Hope to finish this this evening.
