#! /usr/bin/python

from re import finditer, split
import sh
import i3ipc

### UDEV-Regel #####
# KERNEL=="card0", SUBSYSTEM=="drm", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/user/.Xauthority", ENV{SHELL}="/bin/bash", ENV{PATH}="/home/user/bin/:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/lib/jvm/default/bin",RUN+="/home/user/bin/ScreenSwitcher/monitor_switch.py"


# EDID from monitors connected over dockingstation
docking_station=['00ffffffffffff004c2d230534303030271401030e301b782a3581a656489a241250542308008100814081809500a940b30001010101023a801871382d40582c4500dd0c1100001e000000fd00383c1e5111000a202020202020000000fc0053796e634d61737465720a2020000000ff004839415a4130303933380a202000d7',
        '00ffffffffffff004c2d230534303030271401030e301b782a3581a656489a241250542308008100814081809500a940b30001010101023a801871382d40582c4500dd0c1100001e000000fd00383c1e5111000a202020202020000000fc0053796e634d61737465720a2020000000ff004839415a4130303932380a202000d8']

# EDID from laptop monitor
LVDS = ["00ffffffffffff0006af3e210000000021140104901f11780261959c59528f2621505400000001010101010101010101010101010101f82a409a61840c30402a330035ae10000018a51c409a61840c30402a330035ae10000018000000fe0041554f0a202020202020202020000000fe004231343052573032205631200a00d0"]


homedir ="/home/matedealer/"

# i3 config files
i3_config = homedir+".config/i3/config"
i3_docking_config = homedir+".config/i3/docking_config"
i3_laptop_config = homedir+".config/i3/laptop_config"
list = []


mapping=[{"edid":docking_station+LVDS,"xrand_script":homedir+"bin/ScreenSwitcher/docking.sh", "i3_config":i3_docking_config},
         {"edid":LVDS,"xrand_script":homedir+"bin/ScreenSwitcher/docking.sh","i3_config":i3_laptop_config}]


#process =subprocess.Popen(["xrandr","--verbose"], stdout=subprocess.PIPE)
#xrandr_output = str(process.stdout.read())


#  get all EDIDs from all connected monitors
xrandr_output = str(sh.xrandr("--verbose").stdout)
edid_list = [xrandr_output[m.start()+6:m.start()+310].replace("\\t","").replace("\\n","") for m in finditer("EDID", xrandr_output )]


# TODO: reload i3 afterwards

for item in mapping:
    if set(edid_list) == set(item["edid"]):
        sh.Command(item["xrand_script"])()
        sh.cp([item["i3_config"], i3_config])


# if set(edid_list) == set(LVDS):
#     mode = "laptop"
#     sh.Command(homedir+"bin/ScreenSwitcher/laptop_only.sh")()
#     sh.cp([i3_laptop_config, i3_config])
#
# elif set(edid_list) == set(docking_station + LVDS):
#     mode = "docking"
#     sh.Command(homedir+"bin/ScreenSwitcher/docking.sh")()
#     sh.cp([ i3_docking_config, i3_config])
#
# else:
#     mode = "unknown"
#     print("Please configure manually!")
#     exit(0)

with open(i3_config, "r") as f:
    string = f.read()

    # get list with [ workspace , output ]. i3 config is like "workspace 1 output VGA-1"
    list = [[a.strip() for a in split("output",string[m.start()+10:m.end()+6].replace("\n",""))] for m in finditer("workspace .* output", string)]
    print(list)



#Move workspaces and reload config
if list:
    i3 = i3ipc.Connection()
    for workspace in list:
        i3.command("workspace {0}".format(workspace[0]))
        i3.command("move workspace to output {0}".format(workspace[1]))

    i3.command("reload")


