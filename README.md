# robosys2023 plusコマンド
* このコマンドは、標準入力から読み取った数字を足し合わせることができます。

[![test](https://github.com/itukisatou/robosys2023/actions/workflows/test.yml/badge.svg)](https://github.com/itukisatou/robosys2023/actions/workflows/test.yml)

## 実行例
* 以下のように標準入力を渡すと数字を足し合わせることができます。
``` bash
$seq 10 | ./plus
55
```

## インストール方法・使用方法
* このリポジトリを任意のディレクトリ内でクローンしてください。
```
$git clone git@github.com:itukisatou/robosys2023.git
```
* plusに実行権限を付与してください。
```
$chmod +x plus
```
* 任意の数を標準入力してください。

## 必要なソフトウェア
* Python
	* テスト済み: 3.7~3.10

## テスト環境
* Ubuntu 20.04

## ライセンス関連
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます.
* このパッケージは、Ryuichi Ueda由来のコード(© 2023 Ryuichi Ueda)を利用しています.
* このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです.
	* [ryuichiueda/my_slides robosys_2022/lesson4.html#/20](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson4.html#/20)
	* [ryuichiueda/my_slides robosys_2022/lesson3.html#/12](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson3.html#/12)
* © 2023 Ituki Satou
