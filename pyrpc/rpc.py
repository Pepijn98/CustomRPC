import asyncio
import json
import os
import struct
import sys
import time


class DiscordRPC:
    def __init__(self, client_id, verbose):
        if sys.platform == 'linux' or sys.platform == 'darwin':
            self.ipc_path = (os.environ.get('XDG_RUNTIME_DIR', None) or os.environ.get('TMPDIR', None) or
                             os.environ.get('TMP', None) or os.environ.get('TEMP', None) or '/tmp') + '/discord-ipc-0'
            self.loop = asyncio.get_event_loop()
        elif sys.platform == 'win32':
            self.ipc_path = r'\\?\pipe\discord-ipc-0'
            self.loop = asyncio.ProactorEventLoop()
        self.sock_reader = None
        self.sock_writer = None
        self.client_id = client_id
        self.verbose = verbose

    async def read_output(self):
        if self.verbose:
            print("reading output")
        data = await self.sock_reader.read(1024)
        code, length = struct.unpack('<ii', data[:8])
        if self.verbose:
            print('OP Code: {code}; Length: {length}\nResponse:\n{data}\n'.format(code=code, length=length, data=json.loads(data[8:].decode('utf-8'))))

    def send_data(self, op: int, payload: dict):
        if self.verbose:
            print('sending data')
        payload = json.dumps(payload)
        data = self.sock_writer.write(struct.pack('<ii', op, len(payload)) + payload.encode('utf-8'))
        if self.verbose:
            print('response:\n{data}'.format(data=data))

    async def handshake(self):
        if sys.platform == 'linux' or sys.platform == 'darwin':
            self.sock_reader, self.sock_writer = await asyncio.open_unix_connection(self.ipc_path, loop=self.loop)
        elif sys.platform == 'win32':
            self.sock_reader = asyncio.StreamReader(loop=self.loop)
            reader_protocol = asyncio.StreamReaderProtocol(self.sock_reader, loop=self.loop)
            self.sock_writer, _ = await self.loop.create_pipe_connection(lambda: reader_protocol, self.ipc_path)
        self.send_data(0, {'v': 1, 'client_id': self.client_id})
        data = await self.sock_reader.read(1024)
        code, length = struct.unpack('<ii', data[:8])
        if self.verbose:
            print('OP Code: {code}; Length: {length}\nResponse:\n{data}\n'.format(code=code, length=length, data=json.loads(data[8:].decode("utf-8"))))

    def send_rich_presence(self, activity):
        current_time = time.time()
        payload = {
            'cmd': 'SET_ACTIVITY',
            'args': {
                'activity': activity,
                'pid': os.getpid()
            },
            'nonce': '{current_time:.20f}'.format(current_time=current_time)
        }
        self.send_data(1, payload)
        self.loop.run_until_complete(self.read_output())

    def close(self):
        self.send_data(2, {})
        self.sock_writer.close()
        self.loop.close()

    def start(self):
        self.loop.run_until_complete(self.handshake())
