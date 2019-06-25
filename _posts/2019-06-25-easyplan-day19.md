---
layout: post
title: EasyPlan Day 19
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-25
permalink: 2019/06/25/easyplan-day19
---
5:58am  
Since last night, I am now implementing the MVC model piece by piece. Still looking for direct usage or redraw of gantt and populate of wbs from the files and changing them to call methods from the project class which then sends a message that the project has been updated.

This in turns was listened by gui components, wbs and gantt and calls their native methods redraw and populate appropriately. This maybe resource inetnsive in the future, but it will be optimized when all the basic functionalities are implemented.

Also an issue is opened at github, but that's just for me and jam. Other people may also join but we have to talk about the issues in contributions first, as I stated in the earlier posts, this may be turned into a commercial project depending on the turns of events.

3:30pm  
Few branches has now been created to address different issues. The current branch that's been working on is the _bar-dragging_ branch. This is for the issues under the dragging of task bar segments. Moving task segment bars is already working. The issue I am having now id the predecessor lines. Maybe I'll leave this be since an issue is already opened for the predecessor. Still have few tweaks needed on the dragging of bars and updates to the tasks and tasks segments.

Later also, a feature will be added while dragging, a pop-ip info window will show giving informations about the task segments being dragged or selected.
