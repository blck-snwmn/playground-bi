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

| Aspect | Evidence | Streamlit |
|--------|----------|-----------|
| Language | SQL + Markdown | Python |
| UI Definition | Declarative (components in Markdown) | Imperative (Python code) |
| Charts | Built-in components | st.* / Altair / Plotly etc. |
| Template Pages | Dynamic routing with `[param].md` | State management with `st.query_params` |
| Caching | Automatic (at build time) | `@st.cache_data` decorator |
| Deployment | Static site generation possible | Server required |

## License

MIT
