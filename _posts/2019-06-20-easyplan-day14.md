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

7:54pm  
I have now implemented the same code above when the cell at start day is changed. Similar purpose.

8:01pm  
Predecessor lines are now fixed. I created an octhogonal line for orthogonal effect by getting the mid point between the predecessor and successor task. This way, the lines will not be drawn as diagonal. However I found another bug in setting the start day of a task. It doesn't check for it's predecessor.

8:38pm  
Just solved and fixed the bug above. I have to check first the dependency of the task that the start day is being edited before applying the new value. Then apply the predecessor end if necessary or appropriate.
