import os
import subprocess
from subprocess import Popen, PIPE

# java -jar Designite.jar -i <path of the input source folder> -o <path of the output folder>

def _run_designite_java(folder_name, folder_path, designiteJava_jar_path, smells_results_folder):
    out_folder = os.path.join(smells_results_folder, folder_name)
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    # logfile = os.path.join(out_folder, "log.txt")
    proc = Popen(["java", "-jar", designiteJava_jar_path, "-i", folder_path, "-o", out_folder])
   
   # proc = Popen(["C:/Users/Himesh/.jdks/openjdk-18.0.2.1/bin/java", "-jar", designiteJava_jar_path, "-i", folder_path, "-o", out_folder])
    proc.wait()


def _build_project(dir, dir_path):
    print("Attempting compilation...")
    #os.environ['JAVA_HOME']
    is_compiled = False
    pom_path = os.path.join(dir_path, 'pom.xml')
    if os.path.exists(pom_path):
        print("Found pom.xml")
        os.chdir(dir_path)
        my_env = os.environ.copy()
        #my_env["JAVA_HOME"] = "C:/Users/Himesh/.jdks/openjdk-18.0.2.1"
        #proc = Popen(['C:/Program Files/apache-maven-3.8.6-bin/apache-maven-3.8.6/bin/mvn', 'clean', 'install', '-DskipTests'],shell=True,env=my_env)
        proc = Popen(['mvn', 'clean', 'install', '-DskipTests'],shell=True,env=my_env)
        proc.wait()
        is_compiled = True

    gradle_path = os.path.join(dir_path, "build.gradle")
    if os.path.exists(gradle_path):
        print("Found build.gradle")
        my_env = os.environ.copy()
        #my_env["JAVA_HOME"] = "C:/Users/Himesh/.jdks/openjdk-18.0.2.1"
        os.chdir(dir_path)
        proc = Popen(['gradle', 'build','-x','test'],shell=True,env=my_env)
        #proc = Popen(['C:/Users/Himesh/Documents/gradle-6/gradle-6.0/bin', 'build','-x','test'],shell=True,env=my_env)
        proc.wait()
        is_compiled = True
    if not is_compiled:
        print("Did not compile")

def         analyze_repositories(repo_source_folder, smells_results_folder, designiteJava_jar_path):
    for dir in os.listdir(repo_source_folder):
        print("Processing " + dir)
        if os.path.exists(os.path.join(smells_results_folder, dir)):
            print ("\t.. skipping.")
        else:
            _build_project(dir, os.path.join(repo_source_folder, dir))
            _run_designite_java(dir, os.path.join(repo_source_folder, dir), designiteJava_jar_path, smells_results_folder)
    print("Done.")