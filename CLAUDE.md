# playground-bi

BI as Code ツールを試すモノレポ。

## 構成

- `evidence/` - Evidence (SQL/Markdown)
- `streamlit/` - Streamlit (Python)
- `data/` - 共有データ (SuperStore.csv)
- `shared/` - 共有SQL等

## データベース

DuckDB を使用。各ツールから `data/SuperStore.csv` を直接クエリ可能。

## 開発コマンド

```bash
make evidence-dev   # Evidence 開発サーバー
make streamlit-dev  # Streamlit アプリ起動
```

## 注意

- Evidence は Node.js 18+ 必須
- Streamlit は uv でパッケージ管理
- DuckDB ファイル (*.duckdb) は gitignore 対象
