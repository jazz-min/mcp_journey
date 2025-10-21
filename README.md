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
