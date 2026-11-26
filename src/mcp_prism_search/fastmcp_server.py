from fastmcp import FastMCP
from mcp_prism_search.fetch import web_fetch as perform_web_fetch, ddg_deep_search as perform_deep_search
from mcp_prism_search.search import aggregated_search as perform_aggregated_search
from mcp_prism_search.cache import get_cache_stats as _cache_stats, prune_cache as _prune, clear_cache as _clear
from mcp_prism_search.providers import available_providers
from mcp_prism_search.injection import sanitize, wrap

mcp = FastMCP("web-search", version="0.1.0")

@mcp.tool()
async def web_search(query, provider="auto", max_results=10, safe_search="off", time_filter=None, search_window=None, blocked_domains=None, allowed_domains=None, preferred_domains=None):
    available = sorted(available_providers("general"))
    response = await perform_aggregated_search(
        query=query,
        provider=provider if provider in {"auto", "all", *available} else "auto",
        max_results=max_results,
        safe_search=safe_search,
        time_filter=time_filter,
        search_window=search_window,
        blocked_domains=blocked_domains,
        allowed_domains=allowed_domains,
        preferred_domains=preferred_domains,
        kind="general",
    )
    for r in response.results:
        r.title, _ = sanitize(r.title)
        r.snippet, _ = sanitize(r.snippet)
    return response.model_dump(mode="json")

@mcp.tool()
async def web_fetch(url, max_chars=12000):
    response = await perform_web_fetch(url=url, max_chars=max_chars)
    if not response.success:
        raise ValueError(response.error or "Fetch failed")
    sanitized, _ = sanitize(response.content)
    response.content = wrap(response.final_url or url, sanitized)
    return response.model_dump(mode="json")

@mcp.tool()
def cache_stats():
    return _cache_stats()

if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)
