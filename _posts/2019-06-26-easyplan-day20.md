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
