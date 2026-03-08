import asyncio
import sys
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.new_event_loop()
print(f"Loop type: {type(loop)}")
loop.close()
