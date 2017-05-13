# mykpwtool
kindle paper white 1 看pdf文档效果不好。
这个脚本使用kpdf2opt和cpdf进行pdf文档的重新排版。

## 脚本功能
1. 使用cpdf按照pdf bookmark 将不同章节或者指定页码拆分pdf文件
1. 使用k2pdfopt对拆分后的pdf文件转成kpw1的6寸横屏排版。

## 使用方法
1. 将需要排版的pdf书放到mykpwtool目录下,比如叫xx.pdf
1. 执行 python mykpwtool.py xx.pdf
1. 执行完成后，会出现out目录，生成的pdf目标文件存放其中。

## kpdf2opt 命令参数解释
[参数](http://www.willus.com/k2pdfopt/help/options.shtml)

