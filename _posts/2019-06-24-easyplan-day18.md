---
layout: post
title: EasyPlan Day 18
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-24
permalink: 2019/06/24/easyplan-day18
---
8:03pm  
Since me and my colleague decided to collaborate on the project, he suggested that we do the coding in MVC (Model-View-Controller). But even though MVC is more applicable in web development, there is a workaround for it in python applications.

This afternoon, I tried and tested the implementation of ```pubsub``` module in the project. The idea is to make the model sends messages during every change in the object. For instance, on the add task method, here is the implementation of it:

```python
self.tasks.append(task)
pub.sendMessage(EVENT_PROJECT_UPDATED)
```

Then on the gantt chart and wbs components, a subscriber is used to listen to this event.

```python
# gantt
pub.subscribe(self.on_project_updated, EVENT_PROJECT_UPDATED)
```

Here, the method ```on_project_updated``` just redraws the gant chart.
