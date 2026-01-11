# playground-bi

A monorepo for experimenting with BI as Code tools.

## Structure

- `evidence/` - Evidence (SQL/Markdown)
- `streamlit/` - Streamlit (Python)
- `dbt/` - dbt project (PostgreSQL)
- `lightdash/` - Lightdash (Docker Compose)
- `data/` - Shared data (SuperStore.csv)
- `shared/` - Shared SQL files

## Database

- Evidence/Streamlit: DuckDB (`data/SuperStore.csv` を直接参照)
- dbt/Lightdash: PostgreSQL (Docker)

## Development Commands

```bash
# Evidence
make evidence-dev   # Start Evidence dev server

# Streamlit
make streamlit-dev  # Start Streamlit app

# dbt + Lightdash
make lightdash-dev  # Start Lightdash + PostgreSQL (Docker)
make dbt-seed       # Load CSV to PostgreSQL
make dbt-run        # Run dbt models
make dbt-test       # Run dbt tests

# Lightdash CLI (deploy after dbt changes)
cd lightdash
PATH="$(cd ../dbt && uv run which dbt | xargs dirname):$PATH" CI=true npx lightdash deploy --project-dir ../dbt --profiles-dir ../dbt
```

## Notes

- Evidence requires Bun
- Streamlit uses uv for package management
- dbt uses uv for package management (dbt-postgres)
- Lightdash runs on Docker (port 8080)
- Lightdash CLI requires local npm install (`lightdash/package.json`)
- DuckDB files (*.duckdb) are gitignored
