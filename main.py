import requests
import pandas as pd
import logging
import sys
from datetime import datetime


API_URL = "https://api.exchangerate-api.com/v4/latest/"

# プログラム動作のログを記録
def setup_logging():
    logging.basicConfig(
        # INFOで通常情報のログを取得(他：DEBUG(詳細デバッグ),WARNING(警告)など、、、)
        level=logging.INFO,
        # 出力のフォーマット(時間 - ログレベル - メッセージ)
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def fetch_exchange_rates(base_currency):
    # APIに通貨コードを渡すためのURLを作成
    url = API_URL + base_currency

    # API通信などエラーが起きる可能性が高いためtryを使用
    try:
        # APIにアクセスしてデータを取得(timeout=10←10秒以上API応答がなければエラー)
        response = requests.get(url, timeout=10)
        # HTTPSにエラーがあったら例外を出力(404エラーなど)
        response.raise_for_status()

        # APIからJSON情報で帰ってくるため取得
        data = response.json()
        # Pythonの辞書型の["rates"]のみ戻り値として返却
        return data["rates"]

    # エラーはいた場合
    except requests.exceptions.RequestException as e:
        logging.error(f"API取得失敗: {e}")
    # プログラム終了
        sys.exit(1)

# fetch_exchange_ratesの["rates"]を使用
def save_to_csv(rates, base_currency):
    # Pythonの辞書型を成形、タプルの集合に変換
    df = pd.DataFrame(list(rates.items()), columns=["Currency", "Rate"])

    today = datetime.now().strftime("%Y-%m-%d")
    # ファイル名作成
    filename = f"data/exchange_rates_{base_currency}_{today}.csv"

    # CSV保存
    df.to_csv(filename, index=False)
    # ログ出力
    logging.info(f"CSV保存完了: {filename}")


def main():
    # ログ出力
    setup_logging()

    # 実行時に入力された通貨を取得 
    # 引数アリの場合　例：python main.py jpy = 日本の為替レートをCSV出力
    if len(sys.argv) > 1:
        # upperで大文字化
        base_currency = sys.argv[1].upper()
    # 引数ナシの場合(デフォルトでアメリカ)
    else:
        base_currency = "USD"

    # ログ出力
    logging.info(f"基準通貨: {base_currency}")
    # APIを取得(為替レートを引数に設定)
    rates = fetch_exchange_rates(base_currency)

    # CSVに保存
    save_to_csv(rates, base_currency)

# このファイルが直接実行されたときだけ動かす
if __name__ == "__main__":
    main()