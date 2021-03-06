import sys, os
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase, Loader
from direct.task import Task

class ModelTexture(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.RelativPath	 = Filename.fromOsSpecific(os.path.abspath(sys.path[0])).getFullpath()     ## Relative Location  
        self.WallObj          = self.loader.loadModel(self.RelativPath + '/BasicWall.egg')                ## Model Object
        self.Texture1         = self.loader.loadTexture(self.RelativPath + '/BrickTexture.jpg')           ## Texture File
        self.ts               = TextureStage('ts')                                      

        self.WallObj.setPos(0, 25, 0)
        self.WallObj.setScale(8, 0.25, 5)
        self.WallObj.reparentTo(self.render)
        self.WallObj.setTexture(self.ts, self.Texture1)             ## Set Texture 
        self.WallObj.setTexScale(self.ts, 3, 4)
        self.WallObj.setTexHpr(self.ts, 90, 0, 0)
   
ModelTexture().run()
