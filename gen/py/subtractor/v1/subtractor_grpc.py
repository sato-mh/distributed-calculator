# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: subtractor/v1/subtractor.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import subtractor.v1.subtractor_pb2


class SubtractorBase(abc.ABC):

    @abc.abstractmethod
    async def Sub(self, stream: 'grpclib.server.Stream[subtractor.v1.subtractor_pb2.SubRequest, subtractor.v1.subtractor_pb2.SubResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/distributedcalculator.subtractor.v1.Subtractor/Sub': grpclib.const.Handler(
                self.Sub,
                grpclib.const.Cardinality.UNARY_UNARY,
                subtractor.v1.subtractor_pb2.SubRequest,
                subtractor.v1.subtractor_pb2.SubResponse,
            ),
        }


class SubtractorStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Sub = grpclib.client.UnaryUnaryMethod(
            channel,
            '/distributedcalculator.subtractor.v1.Subtractor/Sub',
            subtractor.v1.subtractor_pb2.SubRequest,
            subtractor.v1.subtractor_pb2.SubResponse,
        )
