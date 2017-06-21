#!/usr/bin/env bash
mkdir -p tmp
mv $1 ./tmp
# cd ./tmp; ../cpdf -split -chunk 500 $1 -o @F_@N_@S_@E.pdf
cd ./tmp; ../cpdf -split-bookmarks 0 $1 -o @F_@N_@S_@E.pdf

cd ..
mv ./tmp/$1 .

./k2pdfopt -ui- -mode fw -ls -dev kpw -y -x ./tmp
#./k2pdfopt -ui- -dev kpw -col 2 -ws -1 -evl 1 -m 0.5 ./tmp
#./k2pdfopt -ui- -fc- -dev kpw -wrap- -ws -1 -evl 1 -ls -m 0.5cm -y -x ./tmp

mkdir -p out
mv ./tmp/*k2opt.pdf ./out
rm -rf ./tmp
