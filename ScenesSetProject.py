import maya.cmds as mc
import maya.mel as mel

def Open():
	basicFilter = "All Files(*.*);;MayaFiles(*.ma *.mb);;Maya Ascii(*.ma);;Maya Binary(*.mb);;OBJ(*.obj);;FBX(*.fbx)"
	path = mc.fileDialog2(ff=basicFilter, ds=1, fm=1, cap='open scenes')

	a = path[0]
	b = a.split('/scenes')

	mel.eval('setProject "{}" ;'.format(b[0]))

	fn = mc.file(q=True, sn=True)
	if not fn:
		mc.file(path[0], o=True, f=True)
	else:
		mc.file(s=True)
		mc.file(path[0], o=True)

def consoleKey():
	Open()

Open()
