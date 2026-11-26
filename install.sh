#!/usr/bin/env sh
set -eu

REPO="anywaye/web-search"
BRANCH="${WEB_SEARCH_BRANCH:-master}"

if command -v uv >/dev/null 2>&1; then
  uv tool install "git+https://github.com/${REPO}@${BRANCH}" --force
elif command -v pipx >/dev/null 2>&1; then
  pipx install "git+https://github.com/${REPO}@${BRANCH}" --force
else
  python3 -m pip install --user "git+https://github.com/${REPO}@${BRANCH}"
fi

echo "web-search installed. Add to MCP client: { \"command\": \"web-search\" } (stdio)"
