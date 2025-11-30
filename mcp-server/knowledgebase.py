import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import logging
from fastmcp import FastMCP

from core.utils import call_bailian_model

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('knowledgebase')

# Create an MCP server
mcp = FastMCP("knowledgebase")

# Add an addition tool
@mcp.tool()
def kb_query(query: str) -> dict:
    """
    当用户咨询的问题超出你的认知范围，不可胡编乱造，可以通过关键词检索知识库获取更多的上下文
    Args:
    query: str, 搜索的关键词，多个关键词用空格隔开
    """
    logger.info(f"query: {query}")
    start_time = time.time()
    result = call_bailian_model(query)
    duration = time.time() - start_time
    logger.info(f"result: {result}, duration: {duration:.2f}")
    return {"success": True, "result": result}



# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
