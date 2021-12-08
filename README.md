# Set_project_for_nuke
Set all section from one window. Set project settings manually or automatically from selected node or sections.

HOW TO INSTALL
---
If you have existing "menu.py" or "init.py" please dont touch them!

1. Open "menu.py" and add following codes and save:
    import nuke
    import setWindowMainWindow
    menu = nuke.menu("Nuke")
    nuke_menu = menu.addMenu("Fatih")
    nuke_menu.addCommand("Set project window", "setWindowMainWindow.start()")

2. If you have existing "init.py" file please open it and put the following codes. So, there is no "init.py" please copy and past into ".nuke" folder directly. :
    import nuke
    nuke.pluginAddPath("setProjectWindow")
