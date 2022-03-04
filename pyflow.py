## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


import sys

import discord
from qasync import QEventLoop
from PyFlow.Packages.PyFlowBase.Nodes.onMessage import onMessage
from Qt.QtWidgets import QApplication

from PyFlow.App import PyFlow
from settings import DISCORD_BOT_TOKEN


class Client(discord.Client):

    def __init__(self, instance: PyFlow):
        super().__init__()
        self.instance: PyFlow = instance

    async def on_message(self, message):
        for node in self.instance.getCanvas().graphManager.getAllNodes():
            if isinstance(node, onMessage):
                node.execute(message)

def main():
    app = QApplication(sys.argv)

    instance: PyFlow = PyFlow.instance(software="standalone")
    if instance is not None:
        app.setActiveWindow(instance)
        instance.show()
    loop = QEventLoop(app)
    client = Client(instance)
    loop.create_task(client.start(DISCORD_BOT_TOKEN))
    loop.run_forever()


if __name__ == '__main__':
    main()
