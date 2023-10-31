# VoxelCharacterMaker

# 説明
Besiege向けのスキン、[VoxelCharacter](https://steamcommunity.com/workshop/filedetails/?id=2555529376)の制作を支援するツール   
Blender3.6.4で動作確認

***
# 使い方
## ダウンロード
### ダウンロードするもの
* VoxelCharacterMaker.zip
* template.vox
* Blender
* magicavoxel

### ダウンロード方法
1. VoxelCharacterMaker.zipとtemplate.voxを、このリポジトリの[Releases](https://github.com/Gomanosuke/VoxelCharacterMaker/releases)からダウンロード
1. [Blender](https://www.blender.org/download/)と[magicavoxel](https://ephtracy.github.io/index.html?page=mv_main)を各公式サイトからダウンロード
1. Blenderを開き、編集>プリファレンス>アドオン>インポートからVoxelCharacterMaker.zipを選択し、有効化
1. magicavoxelのローカルフォルダを開き、voxフォルダにtemplate.voxを入れる
***
## モデルの作成
1. magicavoxel.exeがあるフォルダのconfigファイルを開き、objのなかにある〇〇をfalseにする
1. magicavoxelを使ってモデルとテクスチャを制作する
1. exportパネルを開き、任意のフォルダにモデルとテクスチャをエクスポートする

※髪と手などが接していると、離れるようにするためにはBlenderで手作業で修正しないといけないため、予め離れた状態で作ると楽
***
## Blenderのセットアップ
1. Blenderを起動し、ビューポートのツールバーにあるvoxelcharactermakerを開く
1. Skin Folder PAthに"Steam\steamapps\common\Besiege\Besiege_Data\Skins"、Character Nameにキャラクターの名前を設定する
1. Texture Pathにmagicavoxelからエクスポートした画像を指定する
1. "スキンフォルダの作成"ボタンをクリックし、指定したフォルダパスに、キャラクター名のフォルダあり、その中にテクスチャが入ったブロック名のフォルダが有ることを確認する。
1. "OBJをインポート"ボタンからエクスポートしたobjファイルをインポートする
1. "アーマチュアのセットアップ"ボタンをクリックし、モデルにアーマチュアを割り当て、ポーズモードで正しく動かせることを確認する
1. 想定通りに動かない場合は、編集モードやウェイトペイントモードで調整する

***
## ブロックの作成
1. ツールバーの"テンプレートのインポートとスケール変更"からスキンを作成したいブロック名のボタンをクリックする
1. キャラクターのサイズがブロックのサイズに合った大きさに変更され、見本になるデフォルトスキンのブロックが表示されたことを確認する
1. ポーズモードに移り、見本を参考に位置とポーズを調整する
1. オブジェクトモードで、キャラクターのメッシュを選択した状態でツールバーの"エクスポート"から作成したスキンのブロック名のボタンをクリックする
1. "Blenderのセットアップ"で作成したスキンフォルダのブロック名のフォルダに、objファイルが正しくエクスポートされていることを確認する
1. すべてのブロックで繰り返す

***
## ワークショップへのアップロード
1. Besiegeを起動し、スキンが正しく利用できることを確認する
1. 調整が必要な場合は、"ブロックの作成"に戻り作り直す
1. ブロックの選択欄から歯車のマークをクリックする
1. 作成したスキンのSteamマークをクリックする
1. 画面に従い設定を行いアップロードする  

※最初に登録するときはアップロード、更新するときはアップデートをする
