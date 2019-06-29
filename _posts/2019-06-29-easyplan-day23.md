---
layout: post
title: EasyPlan Day 23
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-29
permalink: 2019/06/29/easyplan-day23
---
8:01am  
After driving, I continued to work on the undo/redo feature. This morning, I thought that it might be good to separate the commands on separate files instead on a one big file. This way, I can optimize the memory usage later.

Next is a bug has been added to issues regarding the undo of a task deleted that has a successor. The code must be added on the ```Project``` class to handle the restoration of deleted tasks.

10:52am  
The following are the improvements and added implementations:

- Undo/redo of moving task segment via dialog box
- Undo/redo of dragging task segment
- Dragging task segment now improved by doing the action only if the difference between original position and new is one day.

6:26pm  
Few bug fixes are in placed including restoration of deleted tasks on undo/redo and restoring tasks' successors when needed. Some improvements are that dialog confirmations are removed from Command classes as they are not right to be placed there in the first place.

I will still continue coding tonight and may not logged the latest additions here. Also starting tomorrow, I will be logging the time spent in coding for the project to track my coding efforts.
