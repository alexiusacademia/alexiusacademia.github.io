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

Initially, I finished the general tab for the project information. This should do for now. Later, I will be coding the functionalities for this.

End: 11:38am  

Start: 5:00pm  
To continue, all the initial data is being updated in the project object. When now saved, can be retrieved as the open and save functionality has been updated. The additional properties that can now be set are project name, manager and start date. Finish date is automatically updated based on the duration.
End: 6:09pm  

Start: 9:15pm  
On the spreadsheet control, instead of displaying the day number for the finish column, date is instead displayed based on the project setting start date.

I had to make a few adjustments. First is I wanted the ```Task``` class to have a property for _start_date_ as well and so I added it. But during the saving of tasks list, because I used wx.Datetime, there arises some problems. And so I decided to use python datetime instead as the pickle gracefully pickles it.

Since I changed it, I have to make some convertions during the display of the date since I'm using wx.Datetime on controls displaying dates.
End: --
