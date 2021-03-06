# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: divider/v1/divider.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import divider.v1.divider_pb2


class DividerBase(abc.ABC):

    @abc.abstractmethod
    async def Div(self, stream: 'grpclib.server.Stream[divider.v1.divider_pb2.DivRequest, divider.v1.divider_pb2.DivResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/distributedcalculator.divider.v1.Divider/Div': grpclib.const.Handler(
                self.Div,
                grpclib.const.Cardinality.UNARY_UNARY,
                divider.v1.divider_pb2.DivRequest,
                divider.v1.divider_pb2.DivResponse,
            ),
        }


class DividerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Div = grpclib.client.UnaryUnaryMethod(
            channel,
            '/distributedcalculator.divider.v1.Divider/Div',
            divider.v1.divider_pb2.DivRequest,
            divider.v1.divider_pb2.DivResponse,
        )
