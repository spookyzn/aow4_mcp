from mcp.server.fastmcp import FastMCP
from src.services.tome_service import TomeService
import json

mcp = FastMCP("AOW4_Tomes", log_level="ERROR")


@mcp.tool()
async def list_tomes(use_cache: bool):
    """
    List all available Tomes grouped by category.
    
    Args:
        use_cache: Whether to use cached data or fetch fresh data. (True/False)
        
    Returns:
        A JSON string of Tomes grouped by category.
    """
    tome_service = TomeService()
    tomes = await tome_service.list_tomes(use_cache=use_cache)
    output = [t.to_dict() for t in tomes]
    return json.dumps(output, indent=2)

@mcp.tool()
async def get_tome_detail(name: str, use_cache: bool):

    """
    Get detailed information for a single Tome.
    
    Args:
        name: The name of the Tome to retrieve details for. (例如: The Arch Mage 或者 Transmutation)
        use_cache: Whether to use cached data or fetch fresh data. (True/False)
        
    Returns:
        A JSON string containing the detailed information of the Tome.
    """
    tome_service = TomeService()
    detail = await tome_service.get_tome_detail(name, use_cache=use_cache)
    return json.dumps(detail.to_dict(), indent=2)


if __name__ == "__main__":
    mcp.run(transport='stdio')