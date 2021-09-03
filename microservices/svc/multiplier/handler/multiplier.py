from grpclib.server import Stream
from multiplier.v1.multiplier_grpc import MultiplierBase
from multiplier.v1.multiplier_pb2 import MulRequest, MulResponse


class Multiplier(MultiplierBase):

    async def Mul(self, stream: Stream[MulRequest, MulResponse]) -> None:
        request = await stream.recv_message()
        assert request is not None
        one = float(request.operand_one)
        two = float(request.operand_two)
        result = f'{one * two}'
        await stream.send_message(MulResponse(result=result))
