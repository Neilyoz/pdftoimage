# PDF 内容图片化再打包成 PDF

朋友之前写的一些书籍小作品，总是被篡改内容后加上了被人的名字盗用和贩卖，为了恶心这帮拿来主义者，我就写了一个脚本，主要的作用就是将 PDF 作品先转换成为图片，将每张图片加上水印后，再打包成 PDF 导出。

提高了识别软件识别的难度，也防止了别人复制张贴将 PDF 中的内容轻易拿走。

当然因为使用了 Python 的第三方插件，需要安装

- pipenv
- [poppler](https://poppler.freedesktop.org/)

安装好后

```
git clone https://github.com/Neilyoz/pdftoimage.git
cd pdftoimage
pipenv install
pipenv shell
```

水印图片放命名为 `water_mark.png` 放在 water_logo 就好，把要转的文件放到 source 中

```
python main.py ./source/a.pdf ./target.pdf
```

等待片刻，`target.pdf` 就是输出的文件了。
