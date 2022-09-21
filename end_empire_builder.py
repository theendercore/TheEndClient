import os


def log(s):
    print(s)


input_path = "/media/Data/Game_L/PolyMC/instances/TheEndClient/.minecraft"
output_path = "/home/ender/.local/share/atlauncher/instances/TheEnd"
resourcepacks = ["§cTea", "baguette", "Ender's-Tweaks", "Original Green"]
removed_config_d = [
    ".puzzle_cache",
    "fabric",
    "litematica",
    "minihud",
    "quilt",
    "syncmatica",
    "worldedit",
]
removed_config_f = [
    "cmdkeybindconfig",
    "fzmm",
    "hydra",
    "visible_toggle_sprint",
]
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
        for conf in removed_config_d:
            if dir.startswith(conf):
                os.system('rm -R ' + tmp_path + '/'+dir)
                log("deleted : " + dir)
    for file in files:
        for conf in removed_config_f:
            if file.startswith(conf):
                os.system('rm -R ' + tmp_path + '/'+file)
                log("deleted : " + file)
tmp_path = "./tmp"

# Delete the tmp
x = input("Delte the tmp ?\n")
os.system('rm -r ' + tmp_path)
