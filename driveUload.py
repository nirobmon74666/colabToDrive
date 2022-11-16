from urllib.request import urlopen
from tqdm.auto import tqdm
import requests
import shutil
import os
dirRoot="/content/drive/Shareddrives/Movies/"
os.chdir(dirRoot)
parDirNames= ["Movies","Anime","TV Series","Files"]
typ="type"

def downloadFile(url):
  with requests.get(url, stream=True) as r:
      total_length = int(r.headers.get("Content-Length"))
      with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
          with open(urlopen(url).headers.get_filename().replace("MLWBD.com ",""), 'wb')as output:
              shutil.copyfileobj(raw, output)

def folderDer(ftype):
    foldername=parDirNames[ftype-1]
    return foldername

def folderList():
  print("Folder Lists: ")
  next(os.walk('.'))[1]
  i=0
  while i<len(next(os.walk('.'))[1]):
    print("{}. {}".format((i+1),next(os.walk('.'))[1][i]))
    i=i+1

def fFolderList():
  os.listdir()
  i=0
  while i<len(os.listdir()):
    print("{}. {}".format((i+1),os.listdir()[i]))
    i=i+1

condtn=0
url=input("Enter file URL: ")
while condtn<2:
  condtn+=1
  folderList()
  folSel=int(input("Which {} file you want to upload? :".format(typ).lower()))
  typ=next(os.walk('.'))[1][folSel-1]
  print(typ)
  if typ=="Movies":
    os.chdir(next(os.walk('.'))[1][folSel-1])
    downloadFile(url)
    break
  else:
    os.chdir(next(os.walk('.'))[1][folSel-1])
downloadFile(url)
fFolderList()

