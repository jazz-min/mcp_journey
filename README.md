# mcp_journey
Notes, examples, and experiments from my MCP learning journey

## MCP at a High Level
Large Language Models (LLMs) are incredibly powerful, but they face two key limitations:

* Their knowledge is fixed at the time of training.

* They cannot directly interact with external systems or real-world data.

The Model Context Protocol (MCP),introduced by Anthropic in November 2024,addresses these challenges.
MCP is an open standard that defines a secure and consistent way for LLMs to connect with external data sources, applications, and services.

By using MCP, LLMs can:

* Access up-to-date, real-world data

* Perform actions in external systems

* Tap into specialized tools or features beyond their training scope

## MCP Architecture Overview

The MCP ecosystem involves three main components:

* **MCP Host**: The AI application that coordinates and manages one or more MCP clients.

* **MCP Client**: Connects to an MCP server and retrieves contextual data for the MCP host.

* **MCP Server**: Provides contextual information or actions to the client.

Each **MCP client** maintains a **dedicated one-to-one connection** with its respective **MCP server**, allowing the host to communicate with multiple servers seamlessly.

MCP servers can operate **locally** or **remotely**:

* **Local example**: When Claude Desktop launches the filesystem server using STDIO transport (runs on the same machine).

* **Remote example**: The official Sentry MCP server, which operates on the Sentry platform using HTTP Stream Transport.

## MCP Layers
### Data Layer
Defines the message structure and semantics using a JSON-RPC 2.0–based protocol for consistent communication between clients and servers.

### Transport Layer
Handles connection setup, authentication, and secure communication between MCP participants. It manages how messages are transmitted and framed.

#### Supported Transports

* **STDIO Transport**: Default transport using standard input/output streams.

* **HTTP Stream Transport**: Uses HTTP POST for client-to-server messages and optional Server-Sent Events (SSE) for streaming updates.

* **SSE Transport (Deprecated)**: Older Server-Sent Events–based transport, now replaced by HTTP Stream Transport


## Fast MCP
FastMCP is the standard framework for building MCP applications. The Model Context Protocol (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready with clean, Pythonic code.

### Installation
It's recommended to use uv to install and manage FastMCP. Alternatively, you can use pip.

```pip install fastmcp```

#### Verify Installation
```fastmcp version```

### Quick Start
#### Create a FastMCP Server
[mcp-hello/hello_server.py](mcp-hello/hello_server.py) : A Simple MCP Server that responds with a greeting message.

##### Run the Server
```python hello_server.py```

### Call Your Server
[mcp-hello/hello_client.py](mcp-hello/hello_client.py) : A Simple MCP Client that connects to the server and requests a greeting.
##### Run the Client
```python hello_client.py```



### Core Server Features
* **Tools**: Executable functions that AI applications can invoke to perform actions (e.g., file operations, API calls, database queries)
* **Resources**: Data sources that provide contextual information to AI applications (e.g., file contents, database records, API responses)
* **Prompts**: Reusable templates that help structure interactions with language models (e.g., system prompts, few-shot examples)

### Core Client Features
* **Sampling**: Sampling allows servers to request LLM completions through the client, enabling an agentic workflow. This approach puts the client in complete control of user permissions and security measures
*  **Roots**: Roots allow clients to specify which directories servers should focus on, communicating intended scope through a coordination mechanism.
*  **Elicitation**: Elicitation enables servers to request specific information from users during interactions, providing a structured way for servers to gather information on demand.	


#### The FastMCP Client
* Programmatic client for interacting with MCP servers through a well-typed, Pythonic interface.
* fastmcp.Client class provides a programmatic interface for interacting with any Model Context Protocol (MCP) server, handling protocol details and connection management automatically.
* It helps in various scenarios, including:
 - Testing MCP servers during development 
 - Building deterministic applications that need reliable MCP interactions 
 - Creating the foundation for agentic or LLM-based clients with structured, type-safe operations
* All client operations require using the async with context manager for proper connection lifecycle management.


### CallToolResult Object Overview

When a tool is invoked using the MCP client (e.g., client.call_tool()), it returns a CallToolResult object — a structured response containing both the tool’s output and related metadata.

*Attributes*

| Attribute | Description                                                                                                                                                                                            | 
| :--- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| data | The final, unwrapped result of the tool's execution, in its most accessible format.                                                                                                                    |
| content | A list of MCP-standard content blocks (e.g., TextContent, ImageContent, AudioContent, etc.) returned by the server.                                                                                    | 
| structured_content | Standard JSON-serializable output (dict or list) provided by MCP servers that support structured outputs. Best for most practical use cases.                                                           | 
| is_error | Boolean flag indicating whether the tool execution failed (True = error).                                                                                                                                                                 | 

#### Usage Tips

* Use structured_content when you need to access data fields directly in your code.

* Use content[0].text when you want a readable or printable output.
```
result = client.call_tool("summarize_data", {"file_path": "data.csv"})

# Structured content (for data access)
print(result.structured_content)

# Readable output
print(result.content[0].text)
```

## Example: AI Data Assistant using FastMCP
An AI-powered Data Assistant built using the FastMCP framework, capable of analyzing CSV datasets through standardized Model Context Protocol (MCP) tools.

[Check Github repo](https://github.com/jazz-min/mcp-data-assistant)