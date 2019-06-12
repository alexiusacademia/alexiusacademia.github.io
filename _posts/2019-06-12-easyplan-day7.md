---
layout: post
title: EasyPlan Day 7
author: syncster31
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-12
---
Today is a holiday, so I expect to have a longer time in coding.  

The basic functionalities for the _WBS_ are almost complete. Some of the functions that hasn't been implemented yet are

- Indentation
- (Undo of Indent)
- Undo / Redo
- Automatic fill of End column

Among other things that I'm gonna be coding for today is the gantt chart display. I'm still deciding on what to use as a canvas though. Spent quite some time last night on this and I still haven't yet.

So maybe I'm gonna be coding a little before breakfast and then after that, a lot of time will be put to planning on the next steps ahead.

8:28pm  
To create the canvas, I decided to use the base class ```wx.Window```, also the bars are instance of it. ```Bar``` class is the object the draws the bar segments for each task and draws them to the canvas at the appropriate locations.

9:47pm  
Here comes the debugging. What I have now is that, if I adjust the start day of a task below the first task, it's giving me this error:

```
RecursionError: maximum recursion depth exceeded
```

which is odd by the way because I didn't create a recurssion method in any of my class and the error message just says that and nothing else. I have to do the debugging the hard way. Trial and error!

If I use Painting, the bars will be drawn gracefully and successfully for each operation. But that's not what I wanted. I needed the bars wo be objects, not paint, so that I can handle my own events on each bar segements later.

---

I have found the cause of the RecursionError. Atleast I hope I had. But I still have no way of fixing it. The one that's getting called for about 200 times is the handler for the ```wxEVT_GRID_CELL_CHANGED```. Every call on this calls a method from the controller which in turns call other methods from other class, one of thos is the one that makes the Bar Charts.
