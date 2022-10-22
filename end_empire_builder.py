import os


def log(s):
    print(s)


input_path = "/media/Data/Game_L/PolyMC/instances/TheEndClient/.minecraft"
output_path = "/home/ender/.local/share/atlauncher/instances/TheEndClient"
resourcepacks = ["§cTea", "baguette", "Ender's-Tweaks", "Original Green"]
removed_config = {
    "dir":
    [
        ".puzzle_cache",
        "fabric",
        "litematica",
        "minihud",
        "quilt",
        "syncmatica",
        "worldedit",
    ],
    "file": [
        "cmdkeybindconfig",
        "fzmm",
        "hydra",
        "visible_toggle_sprint",
    ]}
tmp_path = "./tmp"

# Create tmp folder
os.system('mkdir ' + tmp_path)

# Copy the server data
os.system('cp ./perm/servers.dat ' + tmp_path)

# Copy the mods folder and deletes pre-selected and .disabled files
tmp_path += "/mods"
os.system('cp -R ' + input_path + '/mods ' + tmp_path)
os.system('rm -R ' + tmp_path + '/.index ' +
          tmp_path + '/libJNativeHook.x86_64.so')
for root, dirs, files in os.walk(tmp_path):
    for filename in files:
        if filename.endswith(".disabled"):
            log(filename)
            os.system('rm ' + tmp_path + '/' + filename)
tmp_path = "./tmp"

# Copy the resourcepacks (Only the ones in the list)
tmp_path += "/resourcepacks"
os.system('mkdir '+tmp_path)
for root, dirs, files in os.walk(input_path+"/resourcepacks"):
    for rec in resourcepacks:
        for file in files:
            if file.startswith(rec):
                os.system('cp -R \"' + input_path +
                          "/resourcepacks/"+file+"\" " + tmp_path)
                log(file+" | " + rec)
tmp_path = "./tmp"

# Copy the configs folder and delte not need ones
tmp_path += "/config"
os.system('cp -R ' + input_path + '/config ' + tmp_path)
for root, dirs, files in os.walk(input_path+"/config"):
    for dir in dirs:
        for conf in removed_config.get("dir"):
            if dir.startswith(conf):
                os.system('rm -R ' + tmp_path + '/'+dir)
    for file in files:
        for conf in removed_config.get("file"):
            if file.startswith(conf):
                os.system('rm -R ' + tmp_path + '/'+file)
tmp_path = "./tmp"


# Copy the options.txt
os.system('cp ./perm/options.txt ' + tmp_path)

# Delete The old Modpack
for root, dirs, files in os.walk(output_path):
    for dir in dirs:
        os.system('rm -R ' + output_path+"/"+dir)
    for file in files:
        if not file.startswith("instance."):
            os.system("rm -f "+output_path+"/"+file)

# Move The files to the "output_path"
for root, dirs, files in os.walk("./tmp"):
    for dir in dirs:
        os.system('mv ./tmp/'+dir+" "+output_path)
for file in files:
    os.system('mv ./tmp/'+file+" "+output_path)

# Delete the tmp
x = input("Delte the tmp ?\n")
os.system('rm -r ' + tmp_path)
