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
```
[all districts](https://mw-info-api-5.onrender.com/api/mwinfo/districts/)

```
| Endpoint | Method | Description |
|---------|--------|-------------|
| https://mw-info-api-5.onrender.com/api/mwinfo/districts/Lilongwe/ | GET | Full info for Lilongwe |
```
[Lilongwe info](https://mw-info-api-5.onrender.com/api/mwinfo/districts/Lilongwe/)
---

### Agriculture (`/api/agriinfo/`)

```
| Endpoint | Method | Description |
|----------|--------|-------------|
| https://mw-info-api-5.onrender.com/api/agriinfo/query/?name=Chimanga | GET | Search crop or fish by name (Chichewa/English/Scientific) |
```

[query 'chimanga'](https://mw-info-api-5.onrender.com/api/agriinfo/query/?name=Chimanga/)
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
