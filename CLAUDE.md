# playground-bi

A monorepo for experimenting with BI as Code tools.

## Structure

- `evidence/` - Evidence (SQL/Markdown)
- `streamlit/` - Streamlit (Python)
- `data/` - Shared data (SuperStore.csv)
- `shared/` - Shared SQL files

## Database

Uses DuckDB. Each tool can query `data/SuperStore.csv` directly.

## Development Commands

```bash
make evidence-dev   # Start Evidence dev server
make streamlit-dev  # Start Streamlit app
```

## Notes

- Evidence requires Bun
- Streamlit uses uv for package management
- DuckDB files (*.duckdb) are gitignored
