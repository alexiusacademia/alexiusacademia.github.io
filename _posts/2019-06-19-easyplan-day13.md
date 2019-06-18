---
layout: post
title: EasyPlan Day 13
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-19
permalink: 2019/06/19/easyplan-day13
---
6:30am  
I started by accessing the the predecessor's properties and try to recompute. However, I think I have something wrong. I should calculate the new task moved based on the predecessor on the _wbs_ instead on the gantt chart. I will review this later.

Also, I changed the start value to the value indicated in the wbs. I found this as a bug as before, I set the task start as the value minus 1 which is really wrong because on the gantt chart, I also subtracted 1 on the task start on displaying the bars which is redundant.
