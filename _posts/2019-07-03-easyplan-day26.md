---
layout: post
title: EasyPlan Day 26
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-07-03
permalink: 2019/07/03/easyplan-day26
---
Start: 6:19am  
Early morning debugging. Still has some issues with bar dragging. The major change I did was to include the start day for the duration and I'm having lots of issues especially the bar dragging which I'm currently fixing.

6:30am  
I think I just solved the issue with the bar dragging. WBS is now reflecting the correct head start of the bar which is really retrieving the changes to the project object. Next will be the predecessor lines.

Oh just forget something, I didn't fixed the undo function for the bar dragging.

6:41am  
Just fixed the undo/redo for bar dragging. Moving now with the predecessor lines.

6:44am  
Predecessor lines are now fixed. Just a matter of adjusting the start and end points.

End: ---
