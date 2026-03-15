# Exchange Rate Tool

為替レートをAPIから取得してCSVに保存するPythonツールです。

## 機能
・為替レートAPI取得
・CSVファイル保存
・ログ出力

## 必要環境

Python 3.10+

## インストール

pip install -r requirements.txt

## 実行方法

python main.py USD　
(USDの部分は出力したい為替レートの国にしてください例：JPYなど)

## 出力

exchange_rates_USD_2026-03-15.csv
※為替レートの国によって出力されるファイル名(USDの部分)が異なります