---
layout: post
title: Implementing Undo/Redo in wxPython
authors: [alex]
tags: ["python programming", "undo and redo"]
comments: true
like: true
date: 2019-07-04
permalink: 2019/07/04/wxpython-undo-redo
---
When I am about to implement the undo/redo functionality to the desktop application that I'm working on, I thought it's just a matter of creating a do function and magically it will have an undo functionality on its own. Turns out not, obviously. It took me a lot of time looking at references online on implementing this on wxPython but I struggled and did it anyway the hard way. So to help others, I decided to write this entry on how to implement a simple undo/redo functionality in a wxPython application. I hope it'll save you a lot of time searching.

Before continuing, it is required that you have a basic understanding of how a wxPython application work so that we can focus on explaining only what the topic is about and not about creating a window or a frame, etc.

## Command class

Under the ```wx.lib.docview``` package of wxPython, there is a class called ```Command```. What it does is it models an application's Command system. For example, if you have a functionality that adds two numbers, you can put that functionality to a subclass of this ```Command``` class as you should not use it directly. Let's take a look at the code below.

## Custom Command class

**_command_increment.py_**

```python
from wx.lib.docview import Command


class Increment(Command):

    parent = None

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.parent = args[2]

    def Do(self):
        self.parent.number += 2
        return True

    def Undo(self):
        self.parent.number -= 2
        return True
```

## Implementation

The above class is a subclass of the Command class I've mentioned above. So what this does is it increments it's parent's _number_ property by 2. This can be seen in the ```Do``` method. Now to implement the undo, we have to reverse the process and that's why in the ```Undo``` method, 2 (the exact number added) is subtracted from the object property. Notice that both of these methods returns ```True```. This is to tell the application that the Command has been executed or Reversed.  

Now to use this in a GUI application, we will create a bare frame to let us interact with the application.

**_main.py_**

```python
import wx
from wx.lib.docview import CommandProcessor, Command
from command_increment import Increment


class MyFrame(wx.Frame):
    number = 0
    command_processor = None

    def __init__(self):
        super().__init__(parent=None, title='Undo/Redo')
        self.command_processor = CommandProcessor()
        self.init_ui()

    def init_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.txt = wx.TextCtrl(self)
        main_sizer.AddSpacer(5)
        main_sizer.Add(self.txt, flag=wx.EXPAND | wx.RIGHT | wx.LEFT)
        main_sizer.AddSpacer(5)

        btn_add = wx.Button(self, label='Increment')
        btn_undo = wx.Button(self, label='Undo')
        btn_redo = wx.Button(self, label='Redo')

        buttons_sizer.AddSpacer(5)
        buttons_sizer.Add(btn_add)
        buttons_sizer.AddSpacer(2)
        buttons_sizer.Add(btn_undo)
        buttons_sizer.AddSpacer(2)
        buttons_sizer.Add(btn_redo)

        btn_add.Bind(wx.EVT_BUTTON, self.on_increment_clicked)
        btn_undo.Bind(wx.EVT_BUTTON, self.on_undo_clicked)
        btn_redo.Bind(wx.EVT_BUTTON, self.on_redo_clicked)

        main_sizer.Add(buttons_sizer)

        self.SetSizerAndFit(main_sizer)

    def on_increment_clicked(self, event):
        command = Increment(True, 'Increment', self)
        self.command_processor.Submit(command)

        self.txt.SetLabelText(str(self.number))

    def on_undo_clicked(self, event):
        self.command_processor.Undo()
        self.txt.SetLabelText(str(self.number))

    def on_redo_clicked(self, evevnt):
        self.command_processor.Redo()
        self.txt.SetLabelText(str(self.number))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
```

Now, most of the codes in the _main.py_ listing is for creating the user interface. I hope that by this part, you already know what portions I'm talking about.  

Remember the property we are changing from out Increment command? it's the one here:

```python
class MyFrame(wx.Frame):
    number = 0
    ...
```

So we bind the three (3) buttons to different methods. The first one is the ```on_increment_clicked```. In here, we created an instance of our command class then passed the Frame object to it as one of its required parameters. This is retrieved from the _init_ method of the ```Increment``` class. And then we called the Submit method of the command processor to call the ```Do``` method of our custom command class. This places the command object we just created in a stack wherein it can be removed by calling the Undo method of the command processor.

Note that the _CommandProcessor_ is responsible for the commands stack. There are two (2) stacks actually, the one is for _undo_ and the other is for _redo_.

Just a tip, before going through some explanations of tutorials like this, if it contains a working codes/listings like the two in here, copy and run the codes first to test that it's working on your machine. This lessena the frustration later when after reading the whole article and the program won't run, that's just you feel like you lost some motivation already.  

So if available, run the codes first. This helps you motivate when you know that the examples are working just fine.

I hope this helps everyone that comes to the same problem I had regarding this topic. Please let me know about what's your opinion or questions in the comments below.
