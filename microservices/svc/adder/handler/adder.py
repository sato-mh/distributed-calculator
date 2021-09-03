from adder.v1.adder_grpc import AdderBase
from adder.v1.adder_pb2 import AddRequest, AddResponse
from grpclib.server import Stream


class Adder(AdderBase):

    async def Add(self, stream: Stream[AddRequest, AddResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        one = float(request.operand_one)
        two = float(request.operand_two)
        result = f'{one + two}'
        await stream.send_message(AddResponse(result=result))
