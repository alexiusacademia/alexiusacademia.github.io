---
layout: post
title: EasyPlan Day 13
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-19
permalink: 2019/06/19/easyplan-day13
---
6:30am  
I started by accessing the the predecessor's properties and try to recompute. However, I think I have something wrong. I should calculate the new task moved based on the predecessor on the _wbs_ instead on the gantt chart. I will review this later.

Also, I changed the start value to the value indicated in the wbs. I found this as a bug as before, I set the task start as the value minus 1 which is really wrong because on the gantt chart, I also subtracted 1 on the task start on displaying the bars which is redundant.

4:42pm  
As I've notices on Windows, the horizontal grids are erased after the ```redraw``` method has been called. So I tried to use ```wx.CliendDC``` and replaced the ```wx.PaintDC``` in drawling the lines and it works as it should. I'm sticking with it for now and check for Mac later.

Bar movement is also working now when the predecessor of that task has been assigned. The start dat of that task will be set using the ```set_start_day``` method of the Task class instead of just assigning to task.start_day as the method works with all the task segments inside it.

5:01pm  
I have coded now the predecessor line but with bug. The placement in the horizontal direction is incorrect. Another bug I found, not connected to predecessor line, is the setting of predecessor, you cannot unset it. This is maybe on the _wbs_ component. Will work on this later.

5:06pm  
I have reviewed the code and found that it was not a bug on wbs. It's really not going to come back to its original position because the start day of that task is already changed and it has to be changed again for correct placement. I found another lack of implementation though, the start day is not updating after the predecessor is set. I forgot this already as I was focusing on the predecessor lines. This was a problem for me on the previous coding of predecessor as I cannot call the ```populate``` method inside the method of an event inside the same class. So the solution I can think of is manually modifying the content of the cell.

9:40pm  
Just solved the updating of cell start when predecessor is updated. I will also move the start day upon update of any task on duration and start day.
