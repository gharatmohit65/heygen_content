# HeyGen Content SDK (Async) for Python

Asynchronous, typed utilities for the HeyGen Content REST APIs (v1 + v2). Provides:

- Full async/await via httpx
- Pydantic schemas per-route for validation
- Centralized error mapping and auth via a shared HTTP helper (`api/_http.py`)
- Environment-based configuration (`config.py`) and `.env.example`
- Lightweight REST client (`rest_client.py`) and thin singleton client (`client.py`)

## Configuration

Configure via environment variables (or a `.env` file):

```bash
HEYGEN_API_KEY=your_api_key_here
HEYGEN_BASE_URL=https://api.heygen.com/v1
HEYGEN_TIMEOUT=30
```

See `heygen_content/.env.example` for a template.

Access configuration at runtime:

```python
from backend.app.core.third_party_integrations.heygen_content.config import config
print(config.BASE_URL, config.TIMEOUT)
```

## Usage Patterns

### 1) Per-route utilities (recommended)
Each endpoint has a small, focused function using the shared HTTP helper.

```python
from backend.app.core.third_party_integrations.heygen_content.api.v2 import list_supported_languages
langs = await list_supported_languages()
print(langs.languages)
```

More examples:

```python
from backend.app.core.third_party_integrations.heygen_content.api.v1 import (
    list_folders, create_folder, update_folder, trash_folder, restore_folder,
)
from backend.app.core.third_party_integrations.heygen_content.api.v1.schemas import (
    CreateFolderRequest, UpdateFolderRequest,
)

resp = await list_folders(limit=10)
created = await create_folder(CreateFolderRequest(name="My Folder"))
updated = await update_folder(created.data["id"], UpdateFolderRequest(name="Renamed"))
await trash_folder(updated.data["id"]) 
await restore_folder(updated.data["id"]) 
```

### 2) REST client (generic)
Use `HeyGenRESTClient` for generic calls when a utility isn’t available.

```python
from backend.app.core.third_party_integrations.heygen_content.rest_client import HeyGenRESTClient
from backend.app.core.third_party_integrations.heygen_content.api.v1.schemas import ListFoldersResponse

async with HeyGenRESTClient() as rc:
    res = await rc._request("GET", "/v1/folders", ListFoldersResponse)
    print(res)
```

### 3) Thin singleton client
The `client.py` file exposes a thin content client using the same configuration and error mapping.

```python
from backend.app.core.third_party_integrations.heygen_content.client import client
from backend.app.core.third_party_integrations.heygen_content.api.v2.schemas import RemainingQuotaResponse

res = await client.request("GET", "/v2/user/remaining_quota", RemainingQuotaResponse)
print(res.remaining_quota)
```

## Error Handling

Common exceptions (from `api/_exceptions.py`) are raised consistently:

- `AuthenticationError`
- `PermissionDeniedError`
- `NotFoundError`
- `RateLimitError`, `QuotaLimitError`, `CreditNotEnoughError`
- `HeyGenValidationError`
- `ServerError`
- `HeyGenAPIError` (fallback)

## Development

1. Copy `.env.example` to `.env` and fill in values
2. Run tests:

```bash
pytest backend/app/core/third_party_integrations/heygen_content/_tests -q
```

## License

MIT
