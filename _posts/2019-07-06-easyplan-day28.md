---
layout: post
title: EasyPlan Day 28
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-07-06
permalink: 2019/07/06/easyplan-day28
---
Start: 8:30am  
Today, I'm working on the project information dialog box. Just adding some controls on the dialog. First control added to the existing project title and manager is the start date input. This will allow the manager/user to input the start date and this will be the baseline of the timeline of the project.

On the ```Project``` class, I have set the start_date to ```None``` so that the users will be responsible on setting it.

On the ribbon, what I did is to initialize the project start date. Then on saving, since python can't pickle ```wx.DateTime``` objects, I just created tuples from that object. This will now in turn reversed on opening a project file.

End: ---
