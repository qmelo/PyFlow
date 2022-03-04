# from PyFlow.Core import PinBase
# from PyFlow.Core.Common import *
# import discord

# class MessagePin(PinBase):
#     """doc string for MessagePin"""
#     def __init__(self, name, parent, direction, **kwargs):
#         super().__init__(name, parent, direction, **kwargs)
#         self.setDefaultValue(None)

#     @staticmethod
#     def IsValuePin():
#         return True

#     @staticmethod
#     def pinDataTypeHint():
#         return 'MessagePin', None

#     @staticmethod
#     def color():
#         return (0, 0, 0, 255)

#     @staticmethod
#     def supportedDataTypes():
#         return ('MessagePin',)

#     @staticmethod
#     def internalDataStructure():
#         return discord.Message

#     @staticmethod
#     def processData(data):
#         return MessagePin.internalDataStructure()(data)
