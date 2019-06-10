---
layout: post
title: EasyPlan Day 5
author: syncster31
tags: ["easyplan"]
comments: true
like: true
data: 2019-06-10T19:49:00+0800
---
7:49pm  
I resumed coding on the project.
First thing I did was the improvement of the splitter window by applying the live update flag.
Then on the ribbon, instead of using buttons of the contents of ribbon panel, I tried to use toolbars instead and it's more appealing than before so I decided to adapt it.

8:26pm  
Now dinner is over, back to coding while watching IM3. :>
Instead of using the stock bitmaps, free icons are used from ```icons8.com```.

Working on addition of task is not as easy as it seem. I had trouble in adding ```project``` objects as there is a bug in the ```Task``` constructor. Everytime I created a new task, all the tasks inherits the number of segments from the number of task created. The bug was here:

```python
class Task:
    ...
    task_segments = []
    ...

    def __init__(self):
        ...
        ts1 = TaskSegment(0, 1)
        self.task_segments.append(ts1)
```

Instead, it shoud be:

```python
class Task:
    ...
    task_segments = []
    ...

    def __init__(self):
        ...
        ts1 = TaskSegment(0, 1)
        self.task_segments = [ts1]
```
