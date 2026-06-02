# Apple App Store Reviews API: iOS and macOS app reviews as structured JSON

> The most efficient, reliable, and developer-friendly way to use the Apple App Store Reviews API.

**Actor page:** [apify.com/johnvc/apple-app-store-reviews-api](https://apify.com/johnvc/apple-app-store-reviews-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/apple-app-store-reviews-api/input-schema](https://apify.com/johnvc/apple-app-store-reviews-api/input-schema?fpr=9n7kx3)

The Apple App Store Reviews API returns user reviews for any iOS or macOS app as clean, structured JSON: star rating, review title, body text, author, app version, review dates, and helpfulness counts, across 50+ country stores. Target an app by its numeric App Store ID or just by name, sort by most recent, most helpful, most favorable, or most critical, and page through as many or as few reviews as you want. It is built for App Store Optimization (ASO), sentiment analysis, competitor monitoring, churn-signal tracking, and AI agent workflows.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Apple-App-Store-Reviews-API.git
   cd Apify-Apple-App-Store-Reviews-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python apple-app-store-reviews-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python apple-app-store-reviews-api-example.py
```

## Why Use This Apple App Store Reviews API?

**One row per review, ready to analyze.** Every result is a flat JSON object with the rating, title, text, author, version, and dates already separated out. No HTML, no parsing, no cleanup.

**Target by ID or by name.** Pass numeric App Store IDs when you have them, or pass a plain app name and the API resolves it for you. Handy when an agent only knows the app by name.

**iOS and macOS.** The same call works for iPhone, iPad, and Mac apps. Each row is tagged with its platform so mixed runs stay clear.

**Sort the way you need.** Most recent for monitoring, most critical for triage, most helpful for the signal that users themselves upvoted, most favorable for testimonials.

**Localized.** Pull reviews from 50+ country stores to compare sentiment by region or to do localization QA.

**Predictable pay-per-event pricing.** You pay a small setup fee plus a per-review fee, so a quick spot-check costs cents and you only pay for what you receive.

## Features

### Core Capabilities
- Reviews for any iOS or macOS app by numeric ID or by app name
- Four sort orders: most recent, most helpful, most favorable, most critical
- 50+ country stores
- Pagination with a per-app review cap, or unlimited
- Optional ISO date normalization and parsed helpfulness counts

### Data Quality
- Flat, one-review-per-row JSON with consistent field names
- Each row carries its source app ID, country, platform, and sort order
- Helpfulness prose parsed into integer helpful and total counts
- Locale-formatted dates plus an optional ISO 8601 field

## Usage Examples

### Basic Example
```json
{
  "product_ids": ["534220544"],
  "max_reviews": 10
}
```

### Advanced Example
```json
{
  "app_name": "spotify",
  "country": "gb",
  "sort": "mostcritical",
  "max_reviews": 100,
  "start_page": 1,
  "include_macos": true,
  "normalize_dates": true,
  "parse_helpfulness": true
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `product_ids` | `array[str]` | one of | `[]` | Numeric Apple App Store IDs (e.g. `["534220544"]`). Find each ID after `id` in an `apps.apple.com/.../id<NNNNNNNN>` URL. |
| `app_name` | `str` | one of | - | Plain app name (e.g. `netflix`). If `product_ids` is empty, the API resolves the ID and uses the top match. |
| `country` | `str` | no | `us` | Two-letter Apple country store code. Drives the storefront and review locale. 50+ supported. |
| `sort` | `str` | no | `mostrecent` | `mostrecent`, `mosthelpful`, `mostfavorable`, or `mostcritical`. iOS only; macOS always returns most recent. |
| `max_reviews` | `int` | no | `100` | Maximum reviews per app. Set `0` for unlimited (internally capped for safety). Each review returned is billed. |
| `start_page` | `int` | no | `1` | Page to start paginating from. Useful for resuming. |
| `include_macos` | `bool` | no | `true` | Set `false` to skip macOS apps entirely. |
| `normalize_dates` | `bool` | no | `true` | Emit a `review_date_iso` field alongside the locale-formatted date. |
| `parse_helpfulness` | `bool` | no | `true` | Parse `helpful_count` and `total_helpful_count` integers from the helpfulness text. |

At least one of `product_ids` or `app_name` is required.

## Output Format

Each dataset item is one review:

```json
{
  "position_global": 1,
  "position_on_page": 1,
  "review_id": "7417861364",
  "review_title": "Lacks ratios",
  "review_text": "Beautiful app with images and videos but doesn't tell you how much of what goes in making the drink. Needs ratios!",
  "rating": 3,
  "review_date": "Jun 02, 2021",
  "review_date_iso": "2021-06-02",
  "reviewed_version": "Version 3.4.2",
  "helpfulness_text": "3 out of 5 customers found this review helpful",
  "helpful_count": 3,
  "total_helpful_count": 5,
  "author_name": "Punkiepollo",
  "author_id": "100937133",
  "product_id": "534220544",
  "app_platform": "ios",
  "app_country": "us",
  "sort_order": "mostrecent",
  "page_number": 1,
  "total_page_count": 8,
  "fetch_timestamp": "2026-05-26T10:30:00+00:00"
}
```

---

## Use as an MCP tool

You can load the Apple App Store Reviews API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Apple App Store Reviews API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Apple App Store Reviews API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Apple App Store Reviews API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/apple-app-store-reviews-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api`, using OAuth when prompted.
5. Ask Claude to run the Apple App Store Reviews API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Apple App Store Reviews API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/apple-app-store-reviews-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Apple App Store Reviews API to power ASO, sentiment analysis, and competitor monitoring with reliable, structured results.*

Last Updated: 2026.06.02
## n8n integration

Available as an n8n community node, **[n8n-nodes-apple-app-store-api](https://www.npmjs.com/package/n8n-nodes-apple-app-store-api)**. In n8n: Settings, Community Nodes, install `n8n-nodes-apple-app-store-api`, then use it in any workflow (it also works as an AI Agent tool). The node bundles this Actor with the Apple App Store Search and Product APIs as three operations behind one Apify credential.
