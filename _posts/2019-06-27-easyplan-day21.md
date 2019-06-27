---
layout: post
title: EasyPlan Day 21
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-27
permalink: 2019/06/27/easyplan-day21
---
6:49am  
Last night I thought I found a bug. But it's interesting that it's not wrong coding but it's not coded at all yet. It was the task segment, other than first segment, being dragged and not moving. This is fixed now by this block:

```python
# Get the task segment on the left
ts_index = self.task.task_segments.index(self.task_segment)
left_ts_index = ts_index - 1
left_ts: TaskSegment = self.task.task_segments[left_ts_index]
left_limit = (left_ts.start + left_ts.duration) * BAR_SCALE

# Move only to the left if it doesn't overlap
if new_x > left_limit:
    self.project.move_task_segment(self.task, self.task_segment, int(new_x / BAR_SCALE))
    self.Move(self.task_segment.start * BAR_SCALE, self.GetPosition()[1])
```

10:57am  
Working on the vertical grid. I decided to create a variable of major grid interval inside the project class. This can the be saved with the file.
