---
layout: post
title: EasyPlan Day 16
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-22
permalink: 2019/06/22/easyplan-day16
---
7:48am  
This morning, I started on the mouse cursor for task bars. I set it so that it looks like a cursor for moving objects. The only thing that bother mea little bit is it's called ```CURSOR_SIZING``` that's why it was hard to find at first.

The reason I did this is the default action when a bar is hovered is to move its location when dragged.

5:49pm  
I added some validation of project object first on gantt chart and wbs component before drawing them.

5:59pm  
Opening and loading of project now is working. First, I diabled the project object initialization on the creation of main window. Then I've set the project object on opening the file one by one for the main window, left pane and right pane.
