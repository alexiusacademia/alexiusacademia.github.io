---
layout: post
title: EasyPlan Day 3
author: syncster31
tags: ["easyplan"]
comments: true
like: true
---
6:00am  
I resumed the coding of the project. Started at the checking of the splitting of task. Next was getting the duration of the task. Not as straightforward as it may seem. To get the total duration, every task segment needs to get the duration and sum it all up.

7:30am  
I also created a function called ```get_virtual_duration```. This doesn't have to be equal to the total duration. The virtual duration takes the spaces of the splitted task segments and include it as virtual duration. This means that if the task with a total duration of 20 days and splitted at half with a spacing to 10 days, the virtual duration would then be 30 days.

9:08am  
I'm thinking now how to construct the ```set_duration``` function. Thought that was just going to be ```self.set_duration = duration``` but there's more to it than that. Remember that each task comprises of series of segments. So I have three scenarios:

- When the new duration is greater than the previous duration.
- When the new duration is less than the previous duration but the difference is less than the duration of the last segment.
- When the new duration is less than the previous duration but the difference is greater than the duration of the last segment or its succeeding.

9:40am  
Just completed the ```set_duration``` function. Just return ```False``` when the third scenario is encountered.

3:09pm  
Now that I have setup the minimal barebones of the api, I will make the corresponding gui for the project. Since what I selected as a framework is _wxpython_, I have to review its usage and howto's since its a long time when I first messed around with it.

7:24pm  
After a brief review, I started coding on the gui component. First I'm working on the task list pane which I created by subclassing the ```wx.Panel``` window:

```python
class TaskListPane(wx.Panel):
    ...
```

This will be the pane where the tasks definitions will be placed including the action buttons in manipulating each task (e.g. removing, indenting, creating new task)

8:57pm  
After placing the task list pane to the main frame, the ```TaskListPane``` will be improved to put some action buttons like a toolbar.

9:36pm  
Before continuing, I decided to take a step back and study about ribbons. I like the looks of them to be implemented in this application, but I am also open if I could pull a more unique style if ever.

10:38pm  
Here now is the sample of the ribbon drafted:
![alt text](/../assets/images/easyplan/day3/ribbon_preview.png "Ribbon preview")

12:06am  
Time for rest. Ribbon is drawn and the tasks pane well managed in the sizer.
Tomorrow will be the linking of the core api and the gui initially.
