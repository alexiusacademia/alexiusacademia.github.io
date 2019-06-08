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

9:08am  
I'm thinking now how to construct the ```set_duration``` function. Thought that was just going to be ```self.set_duration = duration``` but there's more to it than that. Remember that each task comprises of series of segments. So I have three scenarios:

- When the new duration is greater than the previous duration.
- When the new duration is less than the previous duration but the difference is less than the duration of the last segment.
- When the new duration is less than the previous duration but the difference is greater than the duration of the last segment or its succeeding.
