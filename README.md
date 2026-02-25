# Exchange Rate Tool

## 概要
為替レートをAPIから取得し、CSVファイルとして保存するPythonツールです。

API通信、データ整形、エラー処理を含む実務を想定した構成になっています。

---

## 使用技術

- Python 3.x
- requests
- pandas

---

## 機能

- USD基準の為替レート取得
- JSONデータの解析
- CSVファイル出力
- 例外処理によるエラー対応

---

## セットアップ方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/sh0dev-design/exchange-rate-tool.git
cd exchange-rate-tool
