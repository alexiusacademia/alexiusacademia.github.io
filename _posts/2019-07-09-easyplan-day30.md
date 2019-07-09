---
layout: post
title: EasyPlan Day 30
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-07-09
permalink: 2019/07/09/easyplan-day30
---
Start: 11:30pm  
The other day, last time I conded on the project, I managed to show the timeline dates. However they just every paint event, the project start date is being updated which shall not be happening. Turns out that it's all the pass by reference again that I overlooked. I'm trying to fix it in this little session.

After a few tweaks and changes, I managed to fixed the bug for the timeline. I mistakenly used a wx.Datetime object in initializaing the start date of a project. But this is not really the bug, the bug is really the misuse of passing by referenced object. It's fixed now. Also the object for the project date is set to python ```datetime``` object as to try to remove all instances of ```wx``` on the core package.
End: 12:17am  
