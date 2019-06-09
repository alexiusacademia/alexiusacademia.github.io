---
layout: post
title: EasyPlan Day 4
author: syncster31
tags: ["easyplan"]
comments: true
data: 2019-06-09T08:58:00+0800
---
8:58am  
First thing, is the refactoring the code for the ribbon. What I did is separated the creation of the pages for the ribbon and put them in separate methods (```page_gantt_chart``` etc.).

10:38am  
I have decided to initialize the project from the ```main_frame``` and pass it to the ribbon constructor so that the project object will be accessible to the ribbon class and do all the commands present in the ribbon.
