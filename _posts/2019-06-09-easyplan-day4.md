---
layout: post
title: EasyPlan Day 4
authors: [alex]
tags: ["easyplan"]
comments: true
like: true
date: 2019-06-09T08:58:00+0800
permalink: 2019/06/09/easyplan-day4
---
8:58am  
First thing, is the refactoring the code for the ribbon. What I did is separated the creation of the pages for the ribbon and put them in separate methods (```page_gantt_chart``` etc.).

10:38am  
I have decided to initialize the project from the ```main_frame``` and pass it to the ribbon constructor so that the project object will be accessible to the ribbon class and do all the commands present in the ribbon.

7:58pm  
For continuation, a custom dialog is created to handle the addition of task to the project object. This was donw by subclassing the ```wx.Dialog```. The ```ui``` snippet is as follows:

```python
import wx


class AddTaskDialog(wx.Dialog):
    def __init__(self):
        super().__init__(parent=None, title='Add Task')
        self.panel = wx.Panel(parent=self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        label_task_name = wx.StaticText(self.panel, label='Task Name', size=(100, -1))
        entry_task_name = wx.TextCtrl(self.panel)
        box_task_name = wx.BoxSizer(wx.HORIZONTAL)
        self.add_padding(box_task_name, 5)
        box_task_name.Add(label_task_name, 1)
        box_task_name.Add(entry_task_name, 2)
        self.add_padding(box_task_name, 5)

        label_task_start = wx.StaticText(self.panel, label='Start', size=(100, -1))
        entry_task_start = wx.TextCtrl(self.panel)
        box_task_start = wx.BoxSizer(wx.HORIZONTAL)
        self.add_padding(box_task_start, 5)
        box_task_start.Add(label_task_start, 1)
        box_task_start.Add(entry_task_start, 0)
        self.add_padding(box_task_start, 5)

        label_task_duration = wx.StaticText(self.panel, label='Duration', size=(100, -1))
        entry_task_duration = wx.TextCtrl(self.panel)
        box_task_duration = wx.BoxSizer(wx.HORIZONTAL)
        self.add_padding(box_task_duration, 5)
        box_task_duration.Add(label_task_duration, 1)
        box_task_duration.Add(entry_task_duration, 0)
        self.add_padding(box_task_duration, 5)

        btn_add_task = wx.Button(self.panel, label='Add')
        btn_add_task.SetCursor(wx.Cursor(wx.CURSOR_HAND))
        box_buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.add_padding(box_buttons, 200)
        box_buttons.Add(btn_add_task, 3)
        self.add_padding(box_buttons, 5)

        self.add_padding(self.sizer, 5)
        self.sizer.Add(box_task_name, 0, wx.EXPAND)
        self.add_padding(self.sizer, 5)
        self.sizer.Add(box_task_start, 0, wx.EXPAND)
        self.add_padding(self.sizer, 5)
        self.sizer.Add(box_task_duration, 0, wx.EXPAND)
        self.add_padding(self.sizer, 100)
        self.sizer.Add(box_buttons, 0, wx.EXPAND)

        self.panel.SetSizer(self.sizer)
        self.panel.SetBackgroundColour((100, 200, 50))

    def add_padding(self, sizer, size):
        sizer.AddSpacer(size)
```
