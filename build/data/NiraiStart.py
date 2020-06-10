from panda3d.core import *
import __builtin__, os, sys
import aes

import niraidata

# Config
prc = niraidata.CONFIG
iv, key, prc = prc[:16], prc[16:32], prc[32:]
prc = aes.decrypt(prc, key, iv)

for line in prc.split('\n'):
    line = line.strip()
    if line:
        loadPrcFileData('nirai config', line)

del prc
del iv
del key

# DC
__builtin__.dcStream = StringStream()

dc = niraidata.DC
iv, key, dc = dc[:16], dc[16:32], dc[32:]
dc = aes.decrypt(dc, key, iv)

dcStream.setData(dc)
del dc
del iv
del key

# Resources
# TO DO: Sign and verify the phases to prevent editing.

vfs = VirtualFileSystem.getGlobalPtr()
mfs = [3, 3.5, 4, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13]
abort = False

for mf in mfs:
    filename = 'resources/default/phase_%s.mf' % mf
    if not os.path.isfile(filename):
        print 'Phase %s not found' % filename
        abort = True
        break

    mf = Multifile()
    mf.openRead(filename)

    if not vfs.mount(mf, '/', 0):
        print 'Unable to mount %s' % filename
        abort = True
        break

# Packs
pack = os.environ.get('TT_STRIDE_CONTENT_PACK')
import glob
if pack and pack != 'default':
    print 'Loading content pack', pack
    for file in glob.glob('resources/%s/*.mf' % pack):
        mf = Multifile()
        mf.openReadWrite(Filename(file))
        names = mf.getSubfileNames()
        for name in names:
            ext = os.path.splitext(name)[1]
            if ext not in ['.jpg', '.jpeg', '.ogg', '.rgb']:
                mf.removeSubfile(name)
        vfs.mount(mf, Filename('/'), 0)

if not abort:
    # Run
    import toontown.toonbase.ToontownStart
