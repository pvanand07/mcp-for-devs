from mcp.server.fastmcp import FastMCP
import asyncio

# Create FastMCP server
mcp = FastMCP("fastmcp-sse-server", host="0.0.0.0", port=3000)

@mcp.tool()
async def hello_world(name: str = "World") -> str:
    """Say hello to someone
    
    Args:
        name: The name of the person to greet
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Starting FastMCP SSE server on http://0.0.0.0:3000/sse")
    asyncio.run(mcp.run_sse_async())