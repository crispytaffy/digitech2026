# オープンデータでつくる、わたしのまちマップ

まちのオープンデータを使って、自分だけのオリジナルマップを作るハンズオン教材です。

**データを探す → 整える → GeoJSONに変換する → マップにする →
カスタマイズする**

プログラミングやWeb開発が初めての方でも体験できる内容になっています。

## ハンズオンの概要

Excel / CSV形式のオープンデータをGoogle
Colabで読み込み、Pythonを使ってGeoJSONに変換します。

作成したGeoJSONは、まず **Folium**
を使ってNotebook上のマップに表示します。

その後は、環境に応じて2つの方法でカスタマイズできます。

-   **Google Colab +
    Folium**：生成AIに相談しながら、Notebook上のマップをカスタマイズします。
-   **HTML + Leaflet + GitHub
    Pages（発展編）**：FoliumでGeoJSONが正しく表示できることを確認したあと、同じGeoJSONを使ってWebマップを作成・公開します。

``` text
Excel / CSV
     ↓
   Python
     ↓
   GeoJSON
     ↓
   Folium
     ↓
 ┌──────────────┴──────────────┐
 ↓                             ↓
Foliumでカスタマイズ       HTML + Leaflet
                              ↓
                         GitHub Pages
```

## 教材

  ----------------------------------------------------------------------------------
  ファイル                                  内容
  ----------------------------------------- ----------------------------------------
  [Slide.md](Slide.md)                      ハンズオン本編・Marpスライド

  [Google Colab Notebook](colab/excel_to_geojson.ipynb)                     Excel / CSV → GeoJSON変換・Folium表示

  [AI_CUSTOMIZE.md](AI_CUSTOMIZE.md)        生成AIを使ったFoliumのカスタマイズ方法（Google Colabでのカスタマイズ）

  [GITHUB_PAGES.md](GITHUB_PAGES.md)        HTML + Leaflet + GitHub （PagesによるWeb公開とカスタマイズ）

  [map/](map/)                              Leaflet Webマップのサンプルコード
  ----------------------------------------------------------------------------------

## 必要なもの

-   ノートPC
-   Webブラウザ（Google Chrome推奨）
-   Googleアカウント（Google Colabを使用）

ソフトウェアのインストールは不要です。

ChatGPT、Geminiなどの生成AIがあると、後半のカスタマイズでコードの相談相手として利用できます。

## Sample

サンプルでは、山口県オープンデータカタログサイトで公開されている宇部市「公衆トイレ」データを使用しています。

[Sample「宇部市公衆トイレマップ」](https://crispytaffy.github.io/mymap2026/)

------------------------------------------------------------------------

## License

© 2026 Chie Mizuta

この教材は [Creative Commons Attribution 4.0 International (CC BY
4.0)](https://creativecommons.org/licenses/by/4.0/deed.ja)
のもとで公開しています。

授業・研修・ワークショップ等で、複製・編集・改変・再配布して利用できます。\
利用の際は、原著作者として「Chie Mizuta」の表示をお願いします。

なお、本教材で利用しているオープンデータ、マップ、ライブラリ等の第三者著作物については、それぞれの提供元の利用規約・ライセンスが適用されます。

### 使用データ

サンプルデータとして、宇部市「公衆トイレ」を使用しています。

-   データ提供：宇部市
-   出典：山口県オープンデータカタログサイト「【宇部市】公衆トイレ」
-   ライセンス：Creative Commons Attribution 4.0 International（CC BY
    4.0）
-   データセット：<https://yamaguchi-opendata.jp/ckan/dataset/352021_ubetoile>

### 制作について

本教材の構成、文章およびサンプルコードの作成・編集に、生成AI（ChatGPT）を使用しています。\
内容は制作者が確認・編集した上で公開しています。
