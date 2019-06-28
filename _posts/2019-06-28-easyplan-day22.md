---
layout: post
title: EasyPlan Day 22
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-28
permalink: 2019/06/28/easyplan-day22
---
6:43am  
Today, I may start working on the **undo** and **redo** features. This I think is essential on this program and is a must for implementation. Let's see first if the framework for this that is available in wxPython would be sufficient then I'll stick to it. I don't want to reinvent the wheel and implement my own if they are already available and hopefully reliable.

8:57am  
As a start, I will try to implement undo/redo by using the ```CommandProcessor``` class of the ```wx.lib.docview``` package. Initially, toolbar buttons for undo and redo are added to the ribbon page of gantt chart in the Edit panel.
