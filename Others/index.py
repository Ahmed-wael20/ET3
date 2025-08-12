#  os for file operations
import os
# shutil for moving files and copy them 
import shutil
import sys

# the option we have 

file_type={
    "Images":[".jpg",".png",".jpeg",".gif"],
    "Documents":[".txt",".pdf",".docx"],
    "Videos":[".mp4",".mkv"],
}
simulate=False
if "--simulate" in sys.argv:
     simulate=True
     print(" simulation mode on. No files will be moved \n")
else:
    print(" simulation mode off. Files will be moved \n")

# ask the user to enter the folder path
folder_path = input("enter the folder path to organize: ").strip()
# get file in the folder
# def organize_files(folder_path,simulate=False):
summary={cat:0 for cat in file_type.keys()}
summary["Others"]=0

for file in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file)

    if not os.path.isfile(file_path):
            continue
    
    extension=os.path.splitext(file)[1].lower()
    category="Others"

    for cat,exts in file_type.items():
         if extension in exts:
            category=cat
            break
    

    if simulate:
     print(f"[simulate] would move {file} ->{category}")
    else:
     destination_folder=os.path.join(folder_path,category)
     os.makedirs(destination_folder,exist_ok=True)
     shutil.move(file_path,os.path.join(folder_path,category,file))
     print(f"file {file} moved to {category}")
        
    summary[category]+=1

print("\n the summary:")
for cat,count in summary.items():
    print(f"{cat}:{count} files")


    
