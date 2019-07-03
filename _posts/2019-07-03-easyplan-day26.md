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

7:16am  
A new added functionality is when the duration column is updated, all else is updated accordingly including the newly added column FINISH.

End: 7:17am

Start: 6:30pm  
Just fixed the keyboard shortcuts on Windows. What I did is I also set the accelerators on the main frame and called the commands from the ribbon with the bindings.
End: 6:38pm  

Start: 9:15pm  
On the ```Project``` class, I've editted the method for calculating project duration as the previous was wrong.

The next thing I'm gonna do is add dialog for project information to let users enter informations about the project.
End: --
