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

11:18am  
I have now decided to subclass ```wx.ListCtrl``` and added the ```wx.lib.mixins.listctrl.TextEditMixin``` as parent class to make all the cells editable. The event after editing the cell is already captured and handled in the method ```def on_end_editing(self, event)```.

11:37am  
The project object now is being updated everytime the user has finished editing a cell in the WBS. Some error and bug checking are still to be made.

12:11pm  
Aside from adding a task at the last index, task can now be added at a specified location by selecting a row in the WBS.

Task removal is first implemented from the ribbon commands. A user needs to select a task first, otherwise, an error will be displayed.

The next event I'm going to work on is the scroll event which is included on the style of the ListCtrl object. This will handle the view adjustment of the **WBS** when some parts of it is not visible on the splitter window.

7:12pm  
I am now trying to implement ```wx.Grid``` as the widget for the _work breakdown structure_. I do this by creating a new module ```wbs.py```. 

9:09pm  
Now, the _WBS_ object is working and rows are now appended based on the number of tasks on the project object. The following methods will now be added to the class:
- ```on_end_editing(self, event)``` - Update the project object after editing
- ```on_row_selected(self, event)``` - Set the selected_index on the project object on what row index is selected, this way, we can track which row to work on when executing commands such as inserting task or deleting them.