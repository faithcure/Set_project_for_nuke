import nuke
import setWindowMainWindow
menu = nuke.menu("Nuke")
fmenu = menu.addMenu("MenuName") #Menu name
fmenu.addCommand("clip", "setWindowMainWindow.start()")



