import os
from subprocess import call
import sys

#[program, base, number] = sys.argv

#ALL_REPOS_FILE ="/Users/himesh/Library/CloudStorage/OneDrive-DalhousieUniversity/Thesis/Mootex/run2/eval/final_dataset.csv"
#ALL_REPOS_FILE =base+"final_dataset.csv"
#base ="C:/Users/Himesh/OneDrive - Dalhousie University/Thesis/BroadRelease/final"
base = "/home/himesh/TagCoder"
ALL_REPOS_FILE=base+"/csv/final-dataset.csv"
REPO_STORE_ROOT = base+"/output"
REPOS_TO_DOWNLOAD=2   

def downloadRepo(repoName):
    fullRepoName = "https://github.com/" + repoName + ".git"
    folderName = repoName.replace("/", "_")
    if not os.path.isdir(os.path.join(REPO_STORE_ROOT, folderName)):
        os.mkdir(folderName)
        try:
            call(["git", "clone", "--depth=1", fullRepoName, folderName])
        except:
            print("Exception occurred!!")
            pass

file = open(ALL_REPOS_FILE, 'rt', errors='ignore')
if not os.path.isdir(REPO_STORE_ROOT):
    os.mkdir(REPO_STORE_ROOT)
os.chdir(REPO_STORE_ROOT)
for line in file.readlines()[:REPOS_TO_DOWNLOAD]:
    repo_name = line.strip('\n')
    if not repo_name == "":
        folder_name = repo_name.replace("/", "_")
        folder_path = os.path.join(REPO_STORE_ROOT, folder_name)
        if not os.path.isdir(folder_path):
            print('downloading ' + folder_name)
            downloadRepo(repo_name)
print('Done.')