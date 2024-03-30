# ansiart
## 概要
ansiartは、画像をANSIエスケープシーケンスを用いた文字アートに変換し、コマンドラインインターフェース(CLI)に出力するPythonライブラリです。<br>
また、ANSIエスケープシーケンスをテキストファイルに保存・読み込みする機能も提供します。<br>
デフォルトではTrue colorになっているため、適宜truecolor_to_256color関数を用いて変換してください。
## インストール方法
```shell
pip install ansiart
```
## 提供する関数の一覧
* image_to_ansi
* save_ansi_art
* load_ansi_art
* truecolor_to_256color

## 使用方法
### image_to_ansi : 画像をANSIエスケープシーケンスに変換してCLIに出力
#### 概要
画像のパスを受け取って、その画像をトゥルーカラーのANSIアートに変換します。
#### 引数
1. 画像のパス(str)
2. 表示する画像の横幅(int,デフォルト=150)
3. 表示する画像の縦横比(float,デフォルト=0.5) <br>
   環境によって行間や文字の縦横比が異なるため。
#### 使用方法
```python
from ansiart import image_to_ansi
ansi_art = image_to_ansi("sample.png",150,0.5)
print(ansi_art)
```


### save_ansi_art : ANSIアートをファイルに保存
#### 概要
ANSIアートを受け取り、指定したテキストファイルに保存する。
#### 引数
1. ANSIファイルの保存先(str)
2. 保存するANSIアート(str) 
#### 使用方法
```python
from ansiart import save_ansi_art
save_ansi_art("ansi_art.txt", ansi_art)
```
### load_ansi_art : ファイルからANSIアートを読み込む
#### 概要
テキストファイルからANSIアートを読み込み、それを返す
#### 引数
1. ANSIファイルの場所(str)
#### 使用方法
```python
from ansiart import load_ansi_art
ansi_art = load_ansi_art("ansi_art.txt")
```
### truecolor_to_256color : True colorのANSIアートを256色に変換する
#### 概要
image_to_ansi関数はTrue colorでの表示を基本とするため、サポートしていないターミナル向けにTrue colorのANSIアートを256色のANSIアートに変換します。
#### 引数
1. ANSIアート
#### 使用方法
```python
from ansiart import truecolor_to_256color
ansi_art_256 = truecolor_to_256color(ansi_art)
```

## 貢献方法


貢献したい方は、GitHubでプルリクエストやイシューを開いてください。あらゆる貢献を歓迎します。


## ライセンス


このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。


* * *


# ansiart

## Overview

ansiart is a Python library that converts images into text art using ANSI escape sequences and outputs them to the command line interface (CLI).<br> It also provides the functionality to save and load ANSI escape sequences to and from text files.<br> By default, it uses True color, so use the truecolor\_to\_256color function as needed for conversion.

## Installation
```shell
pip install ansiart
``` 

## List of Functions

-   image\_to\_ansi
-   save\_ansi\_art
-   load\_ansi\_art
-   truecolor\_to\_256color

## Usage

### image\_to\_ansi: Convert an image to ANSI escape sequences and output to CLI

#### Overview

Takes the path of an image and converts that image into True Color ANSI art.

#### Arguments

1.  Path of the image (str)
2.  Width of the image to display (int, default=150)
3.  Aspect ratio of the image to display (float, default=0.5)<br> The line spacing and aspect ratio of characters can vary by environment.

#### Example


```python
from ansiart import image_to_ansi
ansi_art = image_to_ansi("sample.png", 150, 0.5)
print(ansi_art)
``` 

### save\_ansi\_art: Save ANSI art to a file

#### Overview

Takes ANSI art and saves it to a specified text file.

#### Arguments

1.  Path to save the ANSI file (str)
2.  ANSI art to save (str)

#### Example


```python
from ansiart import save_ansi_art
save_ansi_art("ansi_art.txt", ansi_art)
``` 

### load\_ansi\_art: Load ANSI art from a file

#### Overview

Loads ANSI art from a text file and returns it.

#### Arguments

1.  Path to the text file (str)

#### Example



```python
from ansiart import load_ansi_art
ansi_art = load_ansi_art("ansi_art.txt")
```

### truecolor\_to\_256color: Convert True Color ANSI art to 256 colors

#### Overview

Since the image\_to\_ansi function is based on True Color display, this function converts True Color ANSI art to 256 colors ANSI art for terminals that do not support True Color.

#### Arguments

1.  ANSI art

#### Example


```python
from ansiart import truecolor_to_256color
ansi_art_256 = truecolor_to_256color(ansi_art)
```

## Contributing


If you would like to contribute, please open a pull request or issue on GitHub. All contributions are welcome.


## License


This project is released under the MIT License. See the LICENSE file for details.


