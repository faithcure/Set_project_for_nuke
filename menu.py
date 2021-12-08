import nuke
import setWindowMainWindow
import pixelfudger
menu = nuke.menu("Nuke")
fxphd = menu.addMenu("Fatih")
fxphd.addCommand("clip", "setWindowMainWindow.start()")

nuke.menu( 'Nodes' ).addCommand( 'Luma/L_Fuse_v06', lambda: nuke.createNode( 'L_Fuse_v06.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_AlphaClean_v03', lambda: nuke.createNode( 'L_AlphaClean_v03.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_CameraBlur_v01', lambda: nuke.createNode( 'L_CameraBlur_v01.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_Despill_v05', lambda: nuke.createNode( 'L_Despill_v05.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_ExponBlur_v03', lambda: nuke.createNode( 'L_ExponBlur_v03.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_Grain_v05', lambda: nuke.createNode( 'L_Grain_v05.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_SpotRemover_v03', lambda: nuke.createNode( 'L_SpotRemover_v03.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Luma/L_SwitchMatte_v04', lambda: nuke.createNode( 'L_SwitchMatte_v04.gizmo' ) )

nuke.menu( 'Nodes' ).addCommand( 'Fatih/colorPickerID', lambda: nuke.createNode( 'colorPickerID.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Fatih/X_Distort', lambda: nuke.createNode( 'X_Distort.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Fatih/expoglow', lambda: nuke.createNode( 'expoglow.gizmo' ) )
nuke.menu( 'Nodes' ).addCommand( 'Fatih/ITransform', lambda: nuke.createNode( 'ITransform.gizmo' ) )
