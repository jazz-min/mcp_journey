from fastmcp import FastMCP

mcp = FastMCP("Hello Server")


@mcp.tool
def hello(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to FastMCP."


if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    #mcp.run()

    # To use a different transport, e.g., HTTP:
    mcp.run(transport="http", host="127.0.0.1", port=8000)