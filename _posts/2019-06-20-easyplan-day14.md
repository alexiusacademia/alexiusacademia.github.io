---
layout: post
title: EasyPlan Day 14
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-20
permalink: 2019/06/20/easyplan-day14
---
6:06pm  
Earlier this morning, I coded a little and make the task, if it is a successor, move it's start day appropriately if it's predecessor's duration was changed. This afternoon as I'm writing this, I just added an update on the wbs. The update on the start day of a task is reflected automatically.

```python
# Task duration
elif col == 2:
    if value.isdigit():
        task.set_duration(int(value))

        # Move the start days of successor tasks if necessary
        for i, tsk in enumerate(self.project.tasks):
            if tsk.predecessor == index:
                pred_start = task.start_day
                pred_duration = task.get_virtual_duration()
                pred_end = pred_start + pred_duration
                if tsk.start_day < pred_end:
                    tsk.set_start_day(pred_end)
                    self.SetCellValue((i, 1), str(tsk.start_day))
```
