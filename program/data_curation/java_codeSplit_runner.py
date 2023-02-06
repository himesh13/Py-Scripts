import os
import subprocess

def _run_code_split(folder_name, folder_path, code_split_result_folder, code_split_exe_path, code_split_mode):
    out_folder = os.path.join(code_split_result_folder, folder_name).replace("\\","/")
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    print("debug --"+ code_split_exe_path+"||"+folder_path+"||"+out_folder+"||"+code_split_mode)
    #subprocess.call(["C:/Users/Himesh/.jdks/openjdk-18.0.2.1/bin/java", "-jar", code_split_exe_path,
    subprocess.call(["java", "-jar", code_split_exe_path,
    
                     "-i", folder_path, "-o", out_folder, "-m", code_split_mode])

def java_code_split(repo_source_folder, code_split_mode, code_split_result_folder, code_split_exe_path):
    assert code_split_mode == "method" or code_split_mode == "class"
    i = 1
    for dir in os.listdir(repo_source_folder):
        length = len([name for name in os.listdir(repo_source_folder)])
        print("Processing " + dir + "of total "+str(length))
        print("Processing "+str(i) +" of "+str(length))
        i = i+1
        if os.path.exists(os.path.join(code_split_result_folder, dir).replace("\\","/")):
            print ("\t.. skipping.")
        else:
            _run_code_split(dir, os.path.join(repo_source_folder, dir).replace("\\","/"),
                            code_split_result_folder, code_split_exe_path, code_split_mode)
    print("Done.")