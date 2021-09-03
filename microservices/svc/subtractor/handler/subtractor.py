import conf
from adder.v1.adder_grpc import AdderStub
from adder.v1.adder_pb2 import AddRequest
from grpclib.client import Channel
from grpclib.server import Stream
from subtractor.v1.subtractor_grpc import SubtractorBase
from subtractor.v1.subtractor_pb2 import SubRequest, SubResponse


class Subtractor(SubtractorBase):

    async def Sub(self, stream: Stream[SubRequest, SubResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None

        async with Channel(conf.SUBTRACTOR_DAPR_ADDRESS,
                           conf.SUBTRACTOR_DAPR_PORT) as channel:
            adder = AdderStub(channel)
            response = await adder.Add(AddRequest(
                operand_one=request.operand_one,
                operand_two=f'{-1 * float(request.operand_two)}'),
                                       metadata={"dapr-app-id": "svc-adder"})

        await stream.send_message(SubResponse(result=response.result))
