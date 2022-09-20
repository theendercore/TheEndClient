import os


def log(s):
    print(s)


input_path = "/media/Data/Game_L/PolyMC/instances/TheEndClient/.minecraft/"
output_path = "/home/ender/.local/share/atlauncher/instances/TheEnd/"

# os.system('cp -R ' + input_path + ' ./mods')
os.system('cp ./perm/servers.dat '+output_path)





# in_opt = open(input_path + "options.txt", "r")
# in_test_opt = in_opt.read().split('\n')
# exist_opt = open("./perm/options.txt", "r")
# in_exist_opt = exist_opt.read().split()
#
# for in_opt in in_test_opt:
#     for exist_opt in in_exist_opt:
#         if in_opt == exist_opt:
#             # log(in_test_opt)
#             in_exist_opt.remove(exist_opt)
#             in_test_opt.remove(in_opt)
#         # else:
#             # log(exist_opt + " | " + in_opt)
#
# # # log(in_test_opt)
# log(in_exist_opt)
