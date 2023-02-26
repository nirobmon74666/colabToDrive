from urllib import request
from tqdm.auto import tqdm
import requests
import shutil
import os
dirRoot="/content/drive/Shareddrives/Movies/"
os.chdir(dirRoot)
parDirNames= ["Movies","Anime","TV Series","Files"]
typ=""


def downloadFile(url,filename):
  with requests.get(url, stream=True) as r:
      try:
        total_length = int(r.headers.get("Content-Length"))
      except:
        total_length = 0
      with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
          with open(filename.replace("MLWBD.com ",""), 'wb')as output:
              shutil.copyfileobj(raw, output)
          outpt.close()
      raw.close()
def folderDer(ftype):
    foldername=parDirNames[ftype-1]
    return foldername

def folderList():
  print("Folder List: ")
  #next(os.walk('.'))[1]
  i=0
  while i<len(next(os.walk('.'))[1]):
    print("{}. {}".format((i+1),next(os.walk('.'))[1][i]))
    i=i+1

def fFolderList():
  print("Folder & File List: ")
  #os.listdir()
  i=0
  while i<len(os.listdir()):
    print("{}. {}".format((i+1),os.listdir()[i]))
    i=i+1

condtn=0
url=input("Enter file URL: ")
filename=request.urlopen(request.Request(url)).info().get_filename()
if str(filename) == "None":
  filename=input("Enter Filename: ")
while condtn<2:
  condtn+=1
  folderList()
  folSel=int(input("Which {} file do you want to upload? :".format(typ).lower()))
  typ=next(os.walk('.'))[1][folSel-1]
  #print(typ)
  if typ=="Movies":
    os.chdir(next(os.walk('.'))[1][folSel-1])
    break
  else:
    os.chdir(next(os.walk('.'))[1][folSel-1])
downloadFile(url,filename)
fFolderList()

