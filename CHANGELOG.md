# Changelog

## 0.1.0 (2026-11-26)

### Features
- Initial release of `web-search`, forked from isyuricunha/mcp-prism-search.
- Multi-provider aggregated search: bing_html, ddg_html, ddgs (bing/brave/yahoo/yandex), 4get, mwmbl, freeserp, keenable, searxng, wikipedia, hackernews.
- Automatic fallback chain (provider="auto") plus provider="all" fan-out with merge.
- Domain controls: blocked/allowed/preferred domains.
- TTL caching with stats/prune/clear tools.
- web_fetch tool (SSRF-safe fetch with clean extraction).
- ddg_deep_search (search + fetch top pages concurrently).
- Vertical search (wikipedia, hackernews).
- Injection defense: invisible-char stripping + suspicious-pattern detection + <untrusted_content> wrapping on fetched content.
- stdio MCP by default (MCP_TRANSPORT=http for remote).
- Keyless out of the box; keyed providers (Tavily, Exa, Brave, You.com, Serper, Jina) via env vars, skipped when absent.

### Notes
- Not published to PyPI (web-search name likely taken); install via curl installer or pip install git+https://github.com/anywaye/web-search.
