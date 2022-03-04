from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.PyFlowBase.Nodes import FLOW_CONTROL_COLOR


## onMessage node
class onMessage(NodeBase):
    def __init__(self, name):
        super().__init__(name)
        self.out = self.createOutputPin("OUT", 'ExecPin')
        self.message = self.createOutputPin("Message", 'AnyPin')
        self.message.enableOptions(PinOptions.AllowAny)
        self.headerColor = FLOW_CONTROL_COLOR

    def execute(self, message):
        self.message.setData(message)
        self.out.call()

    @staticmethod
    def category():
        return 'Discord'
