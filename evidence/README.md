# Evidence

A BI as Code tool for building dashboards with SQL and Markdown.

## Prerequisites

- [Bun](https://bun.sh/)

## Setup

```bash
# From project root
make evidence-install

# Or directly
cd evidence && bun install
```

## Run Dev Server

```bash
make evidence-dev
# → http://localhost:3000
```

## Directory Structure

```
evidence/
├── pages/                    # Markdown pages
│   ├── index.md              # Home page
│   ├── categories/           # Template pages
│   │   ├── index.md
│   │   └── [category].md
│   ├── input-demo.md
│   ├── conditional-demo.md
│   └── stacked-chart-demo.md
├── sources/                  # Data source configuration
│   └── superstore/
│       └── connection.yaml
└── evidence.plugins.yaml
```

## Demo Pages

| Path | Description |
|------|-------------|
| `/` | Dashboard overview |
| `/categories` | Category analysis (template page) |
| `/input-demo` | Input components demo |
| `/conditional-demo` | Conditional rendering demo |
| `/stacked-chart-demo` | Stacked chart demo |

## Key Features

### SQL Queries

Write SQL in code blocks within Markdown:

````markdown
```sql sales_by_category
SELECT category, SUM(sales) as total_sales
FROM superstore.orders
GROUP BY category
```
````

### Chart Components

```markdown
<BarChart
    data={sales_by_category}
    x=category
    y=total_sales
/>
```

### Input Components

```markdown
<Dropdown
    name=category_filter
    data={categories}
    value=category
/>

WHERE category = '${inputs.category_filter.value}'
```

### Template Pages

Receive URL parameters with `[param].md` filename:

```markdown
<!-- pages/categories/[category].md -->
WHERE category = '${params.category}'
```

## Notes

- **Chart Sorting**: Default sorts by Y-axis descending. Use `sort=false` for time series data
- **ButtonGroup**: Use `valueLabel` instead of `label`

## References

- [Evidence Documentation](https://docs.evidence.dev/)
- [Evidence GitHub](https://github.com/evidence-dev/evidence)
