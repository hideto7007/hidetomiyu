from PIL import Image
import os

dirs = "./images_resize/"

for path in os.listdir(dirs):
    full_path = dirs + path

    # リサイズ前の画像を読み込み
    img = Image.open(full_path)
    # 読み込んだ画像の幅、高さを取得し半分に
    (width, height) = (600, 800)
    # 画像をリサイズする
    img_resized = img.resize((width, height))
    # ファイルを保存
    img_resized.save(dirs + path, quality=90)