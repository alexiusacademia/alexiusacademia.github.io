---
layout: post
title: EasyPlan Day 20
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-26
permalink: 2019/06/26/easyplan-day20
---
6:36am  
Earlier, I made a mistake of assuming that a task can only have one predecessor. I realize last night that it's not limited to one. And so I had to make adjustments.

Late last night, I started the modifications to the codes implementing the predecessors as list instead of a single integer. I mainly worked with the _wbs_ component and made some edits as necessary to ```task.py```, ```project.py``` and this mornig, on the ```gantt.py``` modules.

I found that I had to make additions to the ```project.py``` module as this served as the model and most of the pub messages are being sent from here.

2:44pm  
While at the tour at _Pantabangan Dam_, I was able to do little codings while not mobile. Latest improvement consist of creating two branches, bar-dragging and predecessor. The predecessor branch was didicated to making sure that predecessors are added and fetched correctly. The bar-dragging on the other hand introduced some more modifications. One of those is that setting start day of segment by using the bar location divided by some constant. The new bar location is then finalized after getting the new start day instead on relying on the location of the drag. This then solves the problem with the predecessor lines being disconnected.

6:47pm  
Now I'm at the office, the coding will continue. But first, I had to close some issues in github to announce that those issues are fixed now.

I also added new issue which is a bug I found earlier. The issue is the task bar being allowed moving past its predecessor which is a bug. My bad, I haven't restricted it yet.
