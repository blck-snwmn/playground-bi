.PHONY: help evidence-install evidence-dev streamlit-install streamlit-dev init-db

help:
	@echo "BI as Code Playground"
	@echo ""
	@echo "Usage:"
	@echo "  make evidence-install  - Install Evidence dependencies"
	@echo "  make evidence-dev      - Run Evidence dev server"
	@echo "  make streamlit-install - Install Streamlit dependencies"
	@echo "  make streamlit-dev     - Run Streamlit app"
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
	cd streamlit && uv run streamlit run app.py

# Database
init-db:
	duckdb < shared/init_duckdb.sql
