---
title: カスタムコンポーネント
---

# カスタムコンポーネント

Evidence では Svelte でカスタムコンポーネントを作成できる！

---

## 仕組み

Evidence は **Svelte** ベースなので、`.svelte` ファイルでコンポーネントを作成して使える。

### ディレクトリ構造

コンポーネントは `evidence/components/` に配置：

- `components/MyCard.svelte`
- `components/KPIBox.svelte`

配置すると自動的にページで使用可能になる。

---

## 使い方

1. `components/` フォルダに `.svelte` ファイルを作成
2. Markdown ページで `<ComponentName />` として使用
3. props でデータを渡す

---

## いつカスタムコンポーネントを使う？

| ユースケース | 方法 |
|-------------|------|
| 簡単なスタイル変更 | CSS / インラインスタイル |
| 繰り返しパターン | DataTable や BarChart |
| 複雑なロジック | カスタムコンポーネント |
| 外部ライブラリ統合 | カスタムコンポーネント |
| 企業ブランディング | カスタムコンポーネント |

---

## 注意点

- Svelte の知識が必要
- `evidence/components/` に配置
- 自動的にページで使用可能になる
- Evidence のビルトインコンポーネントは `@evidence-dev/core-components` からインポート

---

## 参考リンク

- [Evidence Custom Components Docs](https://docs.evidence.dev/components/custom-components)
- [Svelte Tutorial](https://svelte.dev/tutorial)
