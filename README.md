# Set project for nuke BETA*
___

### Description
Don't you use a project or pipeline manager system for nuke? But you need set the project(script) settings every per script... it's so boring i know :). You can see all settings in one window. You need just select read node and get auto settings from selected node and you need specific settings...Its easy, just select manual tab and put the values.
This script will you make your job little bit easer. 

HOW TO INSTALL
---
#### If you have existing "menu.py" or "init.py" please dont touch them! or clone and save.

Just do this:

```python
import nuke
import setWindowMainWindow
menu = nuke.menu("Nuke")
nuke_menu = menu.addMenu("Fatih")
```
    
If you have existing **"init.py"** file please open it and put the following codes. So, there is no **"init.py"** file please copy and past into **".nuke"** folder directly. :
```python
import nuke
nuke.pluginAddPath("setProjectWindow")
```
You can use your own menus. Click and more information here!
___

HOW TO USE
---
Tutorial video is coming soon.

