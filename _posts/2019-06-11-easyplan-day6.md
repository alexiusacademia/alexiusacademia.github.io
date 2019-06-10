---
layout: post
title: EasyPlan Day 6
author: syncster31
tags: ["easyplan"]
comments: true
like: true
data: 2019-06-11T06:37:00+0800
---
6:37am  
After a few thinking, I decided to make the WBS table display (```ListCtrl```) editable instead of relying on the custom dialog windows alone. This will make the editing more easier for the use. Haven't tried it before so it would be exciting to implement I guess.

To implement this, I have to create a custom method from the ```TaskListPane``` class to capture and process this event since this class is a subclass of ```wx.Panel``` and not a ```wx.ListCtrl```. My bad. I should have just used the latter earlier and inherit those methods directly. Well let's see if this can be pulled off. If it would be more difficult then I would replace the parent class to ```wx.ListCtrl```.
