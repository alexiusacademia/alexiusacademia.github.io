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

3:07pm  
Another bug was found this morning. When a task duration or start day was changed, it's successor's start day will change as weel, but that successor's successor start day doesn't change accordingly. Perhaps the method I'm using in updating the successor start day must be improved and not change only one but look for all updates.

3:48pm  
Another bug is fixed. Predecessor is erased when erased on wbs.

5:36pm  
Bar segments can now be moved by dragging horizontally. I haven't worked with details yet but this should be a start.

I limit the movement so that the bar segments can only be moved to the left if they haven't reached the boundary yet.

 Next is the updating of the task segment start day or the whole task start dat if the whole task is being moved. Some restrictions are still for implementations though. Another thing is the update of the start day in the wbs table. Changes should be reflected there in realtime.

9:48pm  
I just made some late night bug fixing on the core api. The bug was on setting the task duration less than its previous value and it was pointed by my friend JAM when he was testing the application.
