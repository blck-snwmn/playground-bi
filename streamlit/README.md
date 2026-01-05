# Streamlit

A framework for building interactive data apps with Python.

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)

## Setup

```bash
# From project root
make streamlit-install

# Or directly
cd streamlit && uv sync
```

## Run App

```bash
make streamlit-dev
# → http://localhost:8501
```

## Directory Structure

```
streamlit/
├── main.py             # Main app (Home)
├── pages/              # Multi-page app
│   ├── 1_Categories.py
│   ├── 2_Trends.py
│   └── 3_Stacked_Charts.py
├── pyproject.toml      # uv project config
└── uv.lock
```

## Demo Pages

| Page | Description |
|------|-------------|
| Home | Dashboard overview |
| Categories | Category analysis (with query params) |
| Trends | Trend analysis |
| Stacked Charts | Stacked chart demo |

## Key Features

### Data Loading (DuckDB)

```python
import duckdb

conn = duckdb.connect()
df = conn.execute("""
    SELECT * FROM read_csv('path/to/data.csv')
""").fetchdf()
```

### Caching

```python
@st.cache_data
def load_data():
    # Heavy processing
    return df
```

### Multi-page Apps

Place files in `pages/` directory to automatically add to sidebar.
Control order with numeric prefix in filename.

### Query Parameters (Shareable URLs)

```python
# Read
category = st.query_params.get("category", None)

# Write
st.query_params["category"] = "Technology"
```

### Charts

**Standard charts:**
```python
st.bar_chart(df, x="category", y="sales")
st.line_chart(df, x="month", y="sales")
```

**Altair (for stacked charts etc.):**
```python
import altair as alt

chart = alt.Chart(df).mark_bar().encode(
    x="category:N",
    y="sales:Q",
    color="segment:N"
)
st.altair_chart(chart, use_container_width=True)
```

### Input Widgets

```python
category = st.selectbox("Category", options)
segments = st.multiselect("Segment", options)
metric = st.radio("Metric", ["Sales", "Profit"], horizontal=True)
```

## References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit GitHub](https://github.com/streamlit/streamlit)
