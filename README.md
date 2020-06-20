<h1>SFCスピリッツ2020最終課題</h1>

ゲスト講師の、
今村久美さん/閑歳孝子さん/渡邉康太郎さん/柳澤大輔さん/千葉功太郎さん/松尾卓哉さん/門松貴さん/平尾丈さん/江渡浩一郎さん/小林正忠さん/駒崎弘樹さん

それぞれの講義中に「#SFCスピリッツ」で呟かれたツイートを集め、マルコフ連鎖を用いて文章を作成し、SFC生とゲスト講師が対話するようなプログラムを作成した。これをGit hub上に公開することで最終課題とする。

<h2>使い方</h2>
ダウンロードか、cloneをし、cd engineをした上で、ゲスト講師名.pyで動かせる。
またゲスト講師名_bot.pyでは、こちらからの任意の文章を読み取り返答してくれるプログラムも作成した。

<h3>アルゴリズム</h3>
入力を受け付け、形態素解析をし、名詞や動詞などを受け取りword2vecでランダムに単語抽出した後、マルコフ連鎖で文章作成。その結果を出力する。
