# djangoのSPA用モック
通常の画面付きdjangoではなくdjango-rest-frameworkを用いた
画面とREST通信前提のモック。
+AzureのOPEN-ID connectを用いたAzure認証でのログイン
フロントは別途用意が必要です。
  
(自分はvue.jsでやっていますがお見せできるレベルにコードがなっていないです。。。)


## 初期設定
python3.8 がインストールされてること  
pipenv が使用できること  
vscode に"python", "python-autopip8"がインストールされていること

00-ui の内部ディレクトリに入って  

    pipenv install --dev
    pipenv shell

で環境起動(`pipenv shell`は毎回必要)  

    which python

で path をコピー  
vscode の settings.json 内に  

    { // pythonの設定 "python.pythonPath": "自身のpython path", "python.linting.enabled": true, "python.linting.pylintEnabled": true, "python.linting.lintOnSave": true, "editor.formatOnSave": true, "python.formatting.provider": "autopep8", "python.linting.pylintArgs": [ "--load-plugins=pylint_django", ] }

上記を貼り付け。  
`python.pythonPath`は先ほど取得した path となる

下記コマンドで初期 migration 実行
※テストなので
    
    python manage.py migrate

## 起動
vscodeのデバックよりpython djangoを選択し起動。  
初期設定でlocalのコンフィグが選択されるので  
`./config/settings/local.py`でdbのIPなどご自身のものに修正してください。

また、azureのログイン機能を実行する場合も  
各種パラメータを自身のazureのものに変更してください。  
dummy-loginがあるのでazureなしでも動作可能です。  
(参考:https://docs.microsoft.com/ja-jp/azure/active-directory/develop/v2-protocols-oidc)


## アクセス
アクセス先は`http://lcoalhost:8000`となります。
`./config/settings/url_auth.py`内の
`NON_AUTH_PATH`に記載のあるurlのみ認証無しで接続できます。
認証にはDBにユーザデータが必要となります。
テストだけであれば
`http://lcoalhost:8000/sample/get/`でテストができます。

## UNIT TEST 設定

    python manage.py test --keepdb アプリ名(ex. sample) 

で起動。クラス単位、モジュール単位も可能。その場合は import 形式で.(ドット)でつなぐ  
DBは一々作ると時間がかかってしまうのでkeepdb指定

## Bat 起動

各アプリの management/commands 配下のファイルを起動する
ただしファイル名に.py はつけないので注意。また、各ファイルは Basecommand を継承した Command クラスが
必要となる。  

    python manage.py {{ファイル名}}


