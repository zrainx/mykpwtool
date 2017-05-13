# -*- coding:utf-8 -*-

import sys
import subprocess

if __name__ == '__main__':

    if len(sys.argv)>1:
        subprocess.call("mkdir -p tmp",shell=True)
        subprocess.call("mv "+sys.argv[1]+" ./tmp", shell=True)
        subprocess.call("cd ./tmp", shell=True)
        subprocess.call("cd ./tmp; ../cpdf -split-bookmarks 0 " +sys.argv[1] +" "+"-o @F_@N_@S_@E.pdf",shell=True)
        subprocess.call("mv ./tmp/" + sys.argv[1] + " .", shell=True)
        subprocess.call("./k2pdfopt -ui- -fc- -dev kpw -wrap- -ws -1 -evl 1 -ls -m 0.5cm -y -x ./tmp",shell=True,stdout=open('/dev/null','w'),stderr=subprocess.STDOUT)
        #subprocess.call("./k2pdf.sh",shell=True)
        subprocess.call("mkdir -p out",shell=True)
        subprocess.call("mv ./tmp/*k2opt.pdf ./out", shell=True)
        subprocess.call("rm -rf ./tmp",shell=True)



