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
