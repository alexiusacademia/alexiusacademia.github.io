---
layout: post
title: EasyPlan Day 24
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-30
permalink: 2019/06/30/easyplan-day24
---
Start: 9:40am  
Starting from this day, I will be logging the start and end of coding sessions for the _easyplan_ project.
Added a new entry in the ribbon commands, Merge tool. This merges all the splitted task segments.
End: 10:03am  

Start: 11:11am  
The software is broken :(
End: 12:18pm  

Start: 1:20pm
Starting debugging...

1:42pm  
I just made the merging work and the undo. But the redo has some buggy things going. I can't figure out what yet.

End: 1:45pm  

Start 2:50pm  
Debugging...

To abtract the undo of the merging, I created a new method in the ```Task``` class for unmerging of merged task segment.

Still bug in the merging. Everytime it is merged then undo, the task segments doubles.
End 3:03pm  

Start: 4:00pm  
Start of debugging.

- Undo/Redo bug of merging of task has now been resolved.
- Bud: display of start of segment in wbs is resolved.
- Bug: unable to move task segment towards left when near the boundary is resolved.
End 4:40pm  
