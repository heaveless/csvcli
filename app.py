import asyncio
import threading
from typing import Generic, TypeVar

Returntype = TypeVar("Returntype")

class App(Generic[Returntype], DOMNode):
    pass

    async def _process_messages():
        pass

    async def run_async(self):
        app = self 

        try:
            app._loop = asyncio.get_running_loop()
            app._thread_id = threading.get_ident()
            await app._process_messages()
        finally:
            pass

    def run(self):
        async def run_app():
            self._loop = asyncio.get_running_loop()
            self._thread_id = threading.get_ident()
            try:
                await self.run_async()
            finally:
                self._loop = None
                self._thread_id = 0

        event_loop = asyncio.get_event_loop()
        event_loop.run_until_complete(run_app())