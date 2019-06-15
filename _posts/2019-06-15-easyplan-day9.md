---
layout: post
title: EasyPlan Day 9
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-15
permalink: 2019/06/15/easyplan-day9
---
7:16am  
This is supposed to Day 10, however, I just made one commit yesterday. That commit was making a false bar that simulates a task split. I haven't added any code since  until today.

I made a false bar because I cannot, as of this writing, make the window refresh work. Everytime I call the redraw method from the event triggered by the split method, the application crashes.

7:34am  
Now to work on the task splitting on the gui, I have to modify the core Task class and add the resulting two task segments after splitting the task.

10:46am  
What I have now is, the task can be splitted into two segments, however, during the splitting, thw whole task is moved one day to the right while the gantt chart window has not been refreshed. After the refresh, the task segments now will be in their correct position. One way of splitting the task I implemented is by double clicking on the task at the position appropriate. Below is the snippet of the event handler of that event:

```python
    def on_double_clicked(self, event, task, task_segment):
        if isinstance(event, wx.MouseEvent):
            loc = event.GetPosition()
            x = loc[0]
            day = int(x / BAR_SCALE) + 1
            result = task.split_task(task_segment, day)
            ts1, ts2 = result[1]
            print('ts1:', ts1.start, ts1.duration)
            print('ts2', ts2.start, ts2.duration)
            bs = event.GetEventObject()

            x, y = bs.GetPosition()

            # Delete and hide the source bar segment
            # self.bars.remove(bs)
            bs.Hide()

            for ts in result[1]:
                bs1 = BarSegment(self,
                                 ts.start * BAR_SCALE,
                                 y,
                                 ts.duration * BAR_SCALE,
                                 BAR_HEIGHT, task, ts)
                self.bars.append(bs1)
```

2:39pm  
Instead of invoking the splitting by the double click, I decided to created a dialog window to handle that. This can now called from the ribbon if a task segment is selected.

3:12pm  
The task split is now working after the split dialog is closed. I will add invoke of this dialog on the double click event of a task segment bar. I still have some bugs on the split task method that needs to be fixed. Maybe will work on it this evening.
