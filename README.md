# Malawi Info API

A Django-based microservice API providing **informational access** to structured data about:
- Malawi districts
- Agriculture (crops & fish)
- Currency exchange rates

---

## Features

- Query district-level data (e.g., population, climate, elevation)
- Get agriculture details by Chichewa, English, or scientific name
- Perform basic MWK-to-foreign currency conversions using static rates
- YAML-based data source → SQLite → Django
- Modular microservice design (per app)

---

## Example Endpoints

### Districts (`/api/mwinfo/`)



```
| Endpoint | Method | Description |
|---------|--------|-------------|
| `[all districts](https://mw-info-api-5.onrender.com/api/mwinfo/districts/)` | GET | List all districts |
| `[Lilongwe info](https://mw-info-api-5.onrender.com/api/mwinfo/districts/Lilongwe/`) | GET | Full info for Lilongwe |
```

[all districts](https://mw-info-api-5.onrender.com/api/mwinfo/districts/)
---

### Agriculture (`/api/agriinfo/`)

```
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/agriinfo/query/?name=Chambo` | GET | Search crop or fish by name (Chichewa/English/Scientific) |
```
---

### Currency (`/api/currency/`)
```
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/currency/to_foreign/?amount=10000&currency=USD` | GET | Convert MWK → USD |
| `/currency/to_mwk/?amount=100&currency=ZAR` | GET | Convert ZAR → MWK |
```

## Data Source
- Chatgpt

## License

MIT License — free for personal, academic, and non-commercial use.

## Maintainer

Tuntufye Mwanyongo
