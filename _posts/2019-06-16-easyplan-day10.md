---
layout: post
title: EasyPlan Day 10
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-16
permalink: 2019/06/16/easyplan-day10
---
6:53am  
I added a button in the toolbar with the function to move a task segment. I figure this feature is necessary so I'm adding it. The function is still to be written.

6:41pm  
Moving a task segment is now implemented using a custom dialog similar to the task segment splitting. More on the gantt chart, horizontal grid are also drawn whuch is triggered by the paint event. All bars are now centered vertically on the grid.

Start date is also added to the ```Project``` class for setting and getting the start date. This will also be used in displaying the timeline on top of the gantt chart.
