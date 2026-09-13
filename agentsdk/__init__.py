# agent-sdk-python: typed client for the abc AgentService over easy-rpc.
# AgentServiceClient (generated) wraps easy_rpc Transport; this adds Bearer
# auth and ergonomic error helpers.
from .agent.v1.agent_AgentService_easyrpc_pb2 import AgentServiceClient

class AgentException(Exception):
    def __init__(self, code, message):
        super().__init__(f"agent: code={code} {message}")
        self.code = code
        self.message = message

class AgentClient:
    def __init__(self, transport, token=""):
        self._transport = transport
        _md = {}
        if token:
            _md["authorization"] = [f"Bearer {token}"]
        # generated client uses base transport; inject headers via a wrapper
        self._rpc = AgentServiceClient(_Scoped(self, transport, _md))

    def get_client(self):
        return self._rpc


from .agent.v1.agent_pb2 import *

class _Scoped:
    """Transport wrapper that adds per-request metadata headers."""
    def __init__(self, owner, transport, headers):
        self._t = transport
        self._owner = owner
        self._headers = headers
    async def send(self, req):
        req.headers.update(self._headers)
        return await self._t.send(req)
    async def open_stream(self, req):
        req.headers.update(self._headers)
        return await self._t.open_stream(req)
