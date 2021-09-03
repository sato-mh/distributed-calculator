from divider.v1.divider_grpc import DividerBase
from divider.v1.divider_pb2 import DivRequest, DivResponse
from grpclib.server import Stream


class Divider(DividerBase):

    async def Div(self, stream: Stream[DivRequest, DivResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        one = float(request.operand_one)
        two = float(request.operand_two)
        result = f'{one / two}'
        await stream.send_message(DivResponse(result=result))
