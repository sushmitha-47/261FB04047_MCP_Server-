from mcp.server.mcpserver import MCPServer
mcp = MCPServer("Hello MCP")
@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
@mcp.tool()
def check_even_odd(number: int) -> str:
    """Check whether a number is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"
if __name__ == "__main__":
    mcp.run()