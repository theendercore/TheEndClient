import os


def log(s):
    print(s)


input_path = "/media/Data/Game_L/PolyMC/instances/TheEndClient/.minecraft"
output_path = "/home/ender/.local/share/atlauncher/instances/TheEnd"
tmp_path = "./tmp"

# Create tmp folder
os.system('mkdir ' + tmp_path)

# Copy the server data
os.system('cp ./perm/servers.dat ' + tmp_path)

# Copy the mods folder and deletes pre-selected and .disabled files
# tmp_path += "/mods"
# os.system('cp -R ' + input_path + 'mods ' + tmp_path)
# os.system('rm -R ' + tmp_path + '/.index ' +
#           tmp_path + '/libJNativeHook.x86_64.so')
# for root, dirs, files in os.walk(tmp_path):
#     for filename in files:
#         if filename.endswith(".disabled"):
#             log(filename)
#             os.system('rm ' + tmp_path + '/' + filename)
# tmp_path = "./tmp"

# Copy the configs folder and delte not need ones
tmp_path += "/resourcepacks"
os.system('mkdir '+tmp_path)
resourcepacks = ["§cTea", "baguette", "Ender's-Tweaks", "Original Green"]
for root, dirs, files in os.walk(input_path+"/resourcepacks"):
    for rec in resourcepacks:
        for file in files:
            if file.startswith(rec):
                os.system('cp -R \"' + input_path +"/resourcepacks/"+file+"\" "+ tmp_path)
                log('cp -R \"' + input_path +"/resourcepacks/"+file+"\" "+ tmp_path)
                log(file+" | " + rec)

tmp_path = "./tmp"

# Delete the tmp
x = input("Delte the tmp ?\n")
os.system('rm -r ' + tmp_path)
