import os

output_path = "/home/ender/.local/share/atlauncher/instances/TheEnd/"
input_path = "/media/Data/Game_L/PolyMC/instances/TheEndClient/.minecraft/"

os.system('cp -R ' + input_path + ' ./mods')
