import httpx
from mcp.server.fastmcp import FastMCP

# Create FastMCP server instance (removed logger parameter)
mcp = FastMCP("url-fetcher-server")

@mcp.tool()
async def fetch_url(url: str, max_length: int = 5000) -> str:
    """
    Fetches content from any URL and returns it as text.
    
    Args:
        url: The URL to fetch data from
        max_length: Maximum characters to return (default: 5000)
    
    Returns:
        The fetched content as a string
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            
            content = response.text[:max_length]
            return f"Successfully fetched content from {url}:\n\n{content}"
    except Exception as e:
        return f"Error fetching URL: {str(e)}"

def main():
    # Run the server with stdio transport
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()
