from direct.distributed.DistributedObject import DistributedObject

class Account(DistributedObject):

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
