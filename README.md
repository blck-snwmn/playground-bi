# playground-bi

A monorepo for comparing and evaluating BI as Code tools.

Compare the features and development experience of Evidence and Streamlit using the same data source (SuperStore.csv).

## Structure

```
playground-bi/
├── data/               # Shared data source
│   └── SuperStore.csv
├── evidence/           # Evidence project
├── streamlit/          # Streamlit project
├── dbt/                # dbt project (PostgreSQL)
├── lightdash/          # Lightdash (Docker Compose)
└── shared/             # Shared SQL files
```

See each directory's README for setup and run instructions.

## Data

Uses the SuperStore dataset (retail order data).

| Column | Description |
|--------|-------------|
| Order Date | Order date |
| Category | Product category (Furniture, Office Supplies, Technology) |
| Segment | Customer segment (Consumer, Corporate, Home Office) |
| Sales | Sales amount |
| Profit | Profit amount |
| State | US State |

## Tool Comparison

| Aspect | Evidence | Streamlit | Lightdash |
|--------|----------|-----------|-----------|
| Language | SQL + Markdown | Python | dbt (SQL) + YAML |
| UI Definition | Declarative (Markdown) | Imperative (Python) | GUI + dbt meta |
| Charts | Built-in components | st.* / Altair / Plotly | Built-in (drag & drop) |
| Template Pages | `[param].md` routing | `st.query_params` | Explores/Dashboards |
| Caching | Automatic (build time) | `@st.cache_data` | Query cache |
| Deployment | Static site | Server | Docker (self-host) |
| Data Modeling | SQL files | Python | dbt models |

## License

MIT
