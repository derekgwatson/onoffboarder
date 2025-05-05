# OnOffboarder

A simple internal Flask app to help manage onboarding and offboarding of staff by syncing Google Group membership with our HR system (Employment Hero).

## ✨ Features

- ✅ Pulls active staff list from Employment Hero (via API)
- ✅ Compares with a Google Workspace group (e.g. `all-staff@watsonblinds.com.au`)
- ✅ Identifies and removes emails not on the active list
- ✅ Dry-run mode for safe testing
- ✅ Simple web dashboard to preview and trigger syncs

## 🔧 Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/derekgwatson/onoffboarder.git
   cd onoffboarder
