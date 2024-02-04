import os
import sys
from datetime import datetime

from bs4 import BeautifulSoup


def compile_frontend():
    os.system("cd frontend && npm run build")


def update_line(line):
    soup = BeautifulSoup(line, 'html.parser')
    script = soup.find("script", None)
    if script is not None:
        script["src"] = "/static/remoteController/front" + script["src"]
        return script.prettify().replace("=\"\"", "")
    link = soup.find("link", None)
    if link is not None:
        link["href"] = "/static/remoteController/front" + link["href"]
        return link.prettify().replace("=\"\"", "")
    return line


def update_build():
    index_file = open("./frontend/dist/index.html", "r+")
    lines = index_file.readlines()
    lines.reverse()
    lines.append("{% load static %}\n")
    for x in range(len(lines)):
        line = lines[x]
        lines[x] = update_line(line)
    lines.reverse()
    index_file.seek(0)
    index_file.write("".join(lines))
    index_file.close()


def create_backup():
    if not os.path.exists("./backups"):
        os.system("mkdir ./backups")
    name = "./backups/backup-" + datetime.now().strftime("%Y%m%d%H%M%s")
    os.system("mkdir " + name)
    os.system("cp -Rf src/static/remoteController "+name+"/static/")
    os.system("cp src/remoteController/templates/remoteController/base.html "+name+"/base.html")

    return name


def remove_old_files():
    os.system("rm -Rf ./src/static/remoteController/assets/")
    os.system("rm ./src/remoteController/templates/remoteController/base.html")


def restore_backup(folder):
    os.system("cp -Rf " + folder + "/static/ ./src/static/remoteController/")
    os.system("cp " + folder + "/base.html ./src/remoteController/templates/remoteController/base.html")


def move_files():
    if not os.path.exists("./src/static/remoteController/front"):
        os.system("mkdir ./src/static/remoteController/front")
    for f in os.listdir("./frontend/dist"):
        if f.endswith(".html"):
            os.system("cp ./frontend/dist/index.html ./src/remoteController/templates/remoteController/base.html")
        else:
            os.system("cp -Rf ./frontend/dist/" + f + " ./src/static/remoteController/front/" + f)


def main():
    print("Compiling frontend...")
    compile_frontend()
    print("\nFrontend compiled successfully!\nModifying frontend files to match django settings...")
    update_build()
    print("\nFrontend updated successfully!\nCreating backup...")
    backup = create_backup()
    print("\nBackup created successfully!\nRemoving old files...")
    remove_old_files()
    try:
        print("\nOld files removed successfully!\nMoving new files to server...")
        move_files()
        print("\nMoved new files successfully!\n")
        print("A backup is available at " + backup)
    except Exception as e:
        sys.stderr.write("Something went wrong. Restoring from backup...\n")
        restore_backup(backup)
        print("Restored successfully!\n")



if __name__ == "__main__":
    main()