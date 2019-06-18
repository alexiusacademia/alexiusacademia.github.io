---
layout: post
title: EasyPlan Day 12
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-18
permalink: 2019/06/18/easyplan-day12
---
6:26pm  
First thing I did in the project is added handlers for the new toolbar buttons. Although created, I am still not ready to implement those functionalities. Still deciding on what to use for serializing the object and saving as binary files. 

Aside from my own custom file type, I am also planning to support _Microsoft Project's_ file types as well as _PropjectLibre's_ as they are commonly used today in project planning.

Tonight, I will be working for maybe just one or two hours in the project. I have to give time on my other writing that I started last night while the net is out. Good thing about it though. From time to time you can focus on some things.lol

8:38pm  
Now I've made some change in the ```Task``` class. I changed the default value of predecessor from ```None``` to an empty string. Much easier to work with in python for me.

A new condition was also added in the _wbs_ columns. That is for the predecessors. It will update the task object accordingly.

The next thing I'll work on is the drawing of the predecessor line in the gantt chart. This will help visualize the dependencies of the tasks.
