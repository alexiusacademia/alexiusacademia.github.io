---
layout: post
title: EasyPlan Day 3
author: syncster31
tags: ["easyplan"]
---
6:00am  
I resumed the coding of the project. Started at the checking of the splitting of task. Next was getting the duration of the task. Not as straightforward as it may seem. To get the total duration, every task segment needs to get the duration and sum it all up.

7:30am  
I also created a function called ```get_virtual_duration```. This doesn't have to be equal to the total duration. The virtual duration takes the spaces of the splitted task segments and include it as virtual duration. This means that if the task with a total duration of 20 days and splitted at half with a spacing to 10 days, the virtual duration would then be 30 days.
