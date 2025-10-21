import asyncio
from fastmcp import Client
client = Client("http://localhost:8000/mcp")


async def call_tool(name: str):
    async with client:
        greeting = await client.call_tool("hello", {"name": name})
        print(greeting)

asyncio.run(call_tool("World"))