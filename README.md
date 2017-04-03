**Do not maintain any more**

# About

オレ的ゲーム速報@刃 (http://jin115.com/) から 人気ツイートをスクレイピングして、自動リツイートします。

```
python auto_tweet.py
```

# 実行環境

- macOS 10.12.3
- Python 3.5.2
	- BeautifulSoup4-4.5.3
	- lxml-3.7.2
	- python-twitter-3.2.1

# TODO

- formatting.py が scraping.py を実行してる > 一つのプログラムにする
	- scraping.py のスクレイプ結果の型をstr型にする方法がわからなかったから

- http://jin115.com/archives/#{n}.html から自動で取ってくる
	- n が単純インクリメントでない問題。

# MEMO

- settings.py は別売り
	- 以下フォーマット

```
CONSUMER_KEY = hoge
CONSUMER_SECRET = hoge
ACCESS_TOKEN = hoge
ACCESS_TOKEN_SECRET = hoge
```
