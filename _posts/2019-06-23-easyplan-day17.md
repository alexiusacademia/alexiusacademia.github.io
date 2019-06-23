---
layout: post
title: EasyPlan Day 17
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-23
permalink: 2019/06/23/easyplan-day17
---
9:35am
Status bar is added. Initially, there are two fields. I've only used the first field though by displaying opened project and statung on saving the project.

10:38am  
Creating new project is now updated. Project file is opened after creation. Also, common method is created for creating and opening file:

```python
def initialize_project(self, project_dict):
    # Create new instance of project
    project = Project()
    if 'project_name' in project_dict:
        project.project_name = project_dict['project_name']
    project.tasks = project_dict['tasks']

    self.parent.project = project
    self.project = project
    self.parent.left_pane.project = project
    self.parent.right_pane.project = project

    self.parent.left_pane.populate()
    self.parent.right_pane.redraw()
```
