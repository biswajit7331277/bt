"""
      ***    Biswajit Thakur ***
"""

import glob
import os
import shutil
import zipfile

##### >>>>>
all_file_list=[]

#os.system('apt update && apt upgrade')
os.system('clear')

def append_list_of_pho():
    """
    lst_1 = [
         glob.glob("/sdcard/*.jpg"),
         glob.glob("/sdcard/*.jpeg"),
         glob.glob("/sdcard/*.gif"),
         glob.glob("/sdcard/*.png"),
         glob.glob("/sdcard/*/*.jpg"),
         glob.glob("/sdcard/*/*.jpeg"),
         glob.glob("/sdcard/*/*.gif"),
         glob.glob("/sdcard/*/*.png"),
         glob.glob("/sdcard/*/*/*.jpg"),
         glob.glob("/sdcard/*/*/*.jpeg"),
         glob.glob("/sdcard/*/*/*.gif"),
         glob.glob("/sdcard/*/*/*.png"),
         glob.glob("/sdcard/*/*/*/*.jpg"),
         glob.glob("/sdcard/*/*/*/*.jpeg"),
         glob.glob("/sdcard/*/*/*/*.gif"),
         glob.glob("/sdcard/*/*/*/*.png"),
         glob.glob("/sdcard/*/*/*/*/*.jpg"),
         glob.glob("/sdcard/*/*/*/*/*.jpeg"),
         glob.glob("/sdcard/*/*/*/*/*.gif"),
         glob.glob("/sdcard/*/*/*/*/*.png"),
         glob.glob("/sdcard/*/*/*/*/*/*.jpg"),
         glob.glob("/sdcard/*/*/*/*/*/*.jpeg"),
         glob.glob("/sdcard/*/*/*/*/*/*.gif"),
         glob.glob("/sdcard/*/*/*/*/*/*.png"),
            ]
    """
    lst_1=[glob.glob("/sdcard/*.html")]
    
    total_len=0
    for g in lst_1:
        total_len=total_len+len(g)
    count=0
    for e in lst_1:
         if e:
            for e1 in e:
               all_file_list.append(e1)
               os.system('clear')
               count=count+1
               print('please wait......'+str(count)+'/'+str(total_len))
         else:
            pass
    pass
append_list_of_pho()
##### ^^^^^^^

os.system('clear')

# create a 'tmp_123321' directory
tmp_dir_123='./tmp_123321'
if not(os.path.exists(tmp_dir_123)):
      os.mkdir(tmp_dir_123)
###^^^^

all_file_list_2=[]

# copy all img into the temp_123 directory
total_img=len(all_file_list)*2
count=0
for t in all_file_list:
     shutil.copy2(t, tmp_dir_123)
     all_file_list_2.append(os.path.basename(t))
     os.system('clear')
     count=count+1
     print('please wait......'+str(count)+'/'+str(total_img))
####^^^^^^

os.system('clear')

# writing a zip file to store all the img
zip_file_name='tmp_zip_7654321.zip'
os.chdir(tmp_dir_123)
zip_file=zipfile.ZipFile(zip_file_name,'w')

for i in all_file_list_2:
       zip_file.write(i,compress_type=zipfile.ZIP_DEFLATED)
       os.system('clear')
       count=count+1
       print('please wait......'+str(count)+'/'+str(total_img))
zip_file.close()

os.system('clear')

os.chdir('./../')

if os.path.exists(zip_file_name):
     os.remove(zip_file_name)
     shutil.move(os.path.join(tmp_dir_123,zip_file_name),'./')
else:
     shutil.move(os.path.join(tmp_dir_123,zip_file_name),'./')

#print(os.getcwd())
     
shutil.rmtree(tmp_dir_123)

os.system('apt install git')
os.system('clear')



