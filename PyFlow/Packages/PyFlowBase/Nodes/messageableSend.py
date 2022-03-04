from nine import *
import asyncio

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *


class messageableSend(NodeBase):
    def __init__(self, name):
        super().__init__(name)
        self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
        self.messageable = self.createInputPin('Messageable', 'AnyPin')
        self.messageable.enableOptions(PinOptions.AllowAny)
        self.content = self.createInputPin("content", 'StringPin')
        self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

    @staticmethod
    def category():
        return 'Discord'

    def compute(self, *args, **kwargs):
        task = asyncio.ensure_future(self.messageable.getData().send(content=self.content.getData()))
        task.result()
        self.outExec.call()
