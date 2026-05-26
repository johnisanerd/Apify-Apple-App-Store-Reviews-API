# Dev Notes (internal)

Internal notes for this example repo. This file is published in the public repo, so it must not contain any secret or any upstream data-provider name.

## Source Actor

- Apify store slug: `johnvc/apple-app-store-reviews-api`
- Actor ID: `k3dKElhh0XK52g619`
- Landing page: https://apify.com/johnvc/apple-app-store-reviews-api?fpr=9n7kx3
- MCP server URL (used in all four install sections): `https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api`

## Referral codes

- Apify links carry `?fpr=9n7kx3` (except `docs.`, `mcp.`, `console.` subdomains).
- Cursor links carry `?code=XQP4VBLI3NNX`.
- Claude links use the placeholder token `CLAUDE_REFERRAL`. TODO: replace `CLAUDE_REFERRAL` with the real Claude referral code once one exists. Currently appears on `claude.ai/download`, `claude.ai/code`, and `claude.ai` links in the README install sections.

## Screenshots

TODO: the four files under `screenshots/` are currently PLACEHOLDERS (flat panels) and must be replaced with real captures. Keep the exact filenames so the README embeds keep working.

Capture source: the Actor-scoped Apify MCP configurator at the MCP server URL above. Open it (signed in), scroll to the "Client setup" section, and select each tab:

| File | Configurator tab |
|------|------------------|
| `screenshots/01-claude-cowork-desktop.png` | Claude Desktop |
| `screenshots/02-claude-code.png` | Claude Code |
| `screenshots/03-claude-website.png` | Claude.ai |
| `screenshots/04-cursor.png` | Cursor |

The configurator already shows all four tabs with this Actor preloaded and the URL `https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api`. Crop each shot to the client-setup panel for legibility, then commit over the placeholder of the same name.

## Example run cost

The Python example uses `product_ids: ["534220544"]` with `max_reviews: 10` to keep the first run cheap. Raise `max_reviews`, add product IDs, or set `max_reviews: 0` for unlimited once budget is known.

## Maintenance

- Keep the README parameters table and output block in sync with the Actor's live input schema and output if the Actor changes.
- Re-run the pre-push grep suite before every push: call it an API (never the banned tool word), no upstream vendor name, no em dashes, referral codes present.

Last Updated: 2026.05.26
