# SearchTweet
## 概要
pythonでTwitterのつぶやきを取得する。

## 環境
- python(pipenv):3.7
- python-dotenv:0.13.0
- requests_oauthlib:1.3.0

## 使い方
### API利用申請およびアプリ情報登録
Twitter APIの利用には申請が必要となる。

https://developer.twitter.com/

申請に関しては以下のページなど参考になる。(2020/05時点)
- https://qiita.com/kngsym2018/items/2524d21455aac111cdee
- https://www.itti.jp/web-direction/how-to-apply-for-twitter-api/
- https://digitalnavi.net/internet/3072/

### clone
```
git clone https://github.com/winsb/SearchTweet.git
```

### APIキー、トークン設定(.env)
config/.env.sample を config/.env にコピーする。

.env を開いてアプリ情報登録で取得したAPIキー、トークンを入力する。
```
CONSUMER_KEY=*********************
CONSUMER_SECRET=*********************
ACCESS_TOKEN=*********************
ACCESS_TOKEN_SECRET=*********************
```

### 仮想環境インストール
Pipfileのあるディレクトリで以下のコマンドを入力する。
```
pipenv install
```

### 動作確認
インストールと同じディレクトリで以下のコマンドを入力する。
```
pipenv shell
python main.py
pipenv exit
```
API利用申請で登録したアカウントのホームタイムライン表示されたらAPIの利用が可能である。

## Language support
Japanese only.

## License
This library is under the MIT License.

## Reference
- https://developer.twitter.com/en/docs/api-reference-index
- https://quzee.hatenablog.com/entry/2016/05/08/232539