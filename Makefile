.PHONY: help evidence-install evidence-dev streamlit-install streamlit-dev init-db \
	dbt-install dbt-seed dbt-run dbt-test dbt-docs lightdash-dev lightdash-down

help:
	@echo "BI as Code Playground"
	@echo ""
	@echo "Usage:"
	@echo "  make evidence-install  - Install Evidence dependencies"
	@echo "  make evidence-dev      - Run Evidence dev server"
	@echo "  make streamlit-install - Install Streamlit dependencies"
	@echo "  make streamlit-dev     - Run Streamlit app"
	@echo "  make dbt-install       - Install dbt dependencies"
	@echo "  make dbt-seed          - Load CSV to PostgreSQL"
	@echo "  make dbt-run           - Run dbt models"
	@echo "  make dbt-test          - Run dbt tests"
	@echo "  make dbt-docs          - Generate and serve dbt docs"
	@echo "  make lightdash-dev     - Start Lightdash (Docker)"
	@echo "  make lightdash-down    - Stop Lightdash"
	@echo "  make init-db           - Initialize DuckDB from CSV"

# Evidence (bun)
evidence-install:
	cd evidence && bun install

evidence-dev:
	cd evidence && bun run dev

# Streamlit
streamlit-install:
	cd streamlit && uv sync

streamlit-dev:
	cd streamlit && uv run streamlit run main.py

# dbt
dbt-install:
	cd dbt && uv sync

dbt-seed:
	cd dbt && uv run dbt seed

dbt-run:
	cd dbt && uv run dbt run

dbt-test:
	cd dbt && uv run dbt test

dbt-docs:
	cd dbt && uv run dbt docs generate && uv run dbt docs serve

# Lightdash
lightdash-dev:
	cd lightdash && docker compose up

lightdash-down:
	cd lightdash && docker compose down

# Database
init-db:
	duckdb < shared/init_duckdb.sql
