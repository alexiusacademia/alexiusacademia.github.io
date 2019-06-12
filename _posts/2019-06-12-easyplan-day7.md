---
layout: post
title: EasyPlan Day 7
author: syncster31
tags: ["easyplan"]
comments: true
like: true
data: 2019-06-12T07:31:00+0800
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
