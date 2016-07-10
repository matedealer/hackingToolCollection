#! /usr/bin/python

from re import finditer, split
import sh
import i3ipc

### UDEV-Regel #####
# KERNEL=="card0", SUBSYSTEM=="drm", ENV{DISPLAY}=":0", ENV{XAUTHORITY}="/home/user/.Xauthority", ENV{SHELL}="/bin/bash", ENV{PATH}="/home/user/bin/:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/lib/jvm/default/bin",RUN+="/home/user/bin/ScreenSwitcher/monitor_switch.py"


# EDID from monitors connected over dockingstation
docking_station=[]

# EDID from laptop monitor
LVDS = []

homedir ="/home/user/"

# i3 config files
i3_config = homedir+".config/i3/config"
i3_docking_config = homedir+".config/i3/docking_config"
i3_laptop_config = homedir+".config/i3/laptop_config"
list = []

#  get all EDIDs from all connected monitors
xrandr_output = str(sh.xrandr("--verbose").stdout)
edid_list = [xrandr_output[m.start()+6:m.start()+310].replace("\\t","").replace("\\n","") for m in finditer("EDID", xrandr_output )]


if set(edid_list) == set(LVDS):
    mode = "laptop"
    sh.Command(homedir+"bin/ScreenSwitcher/laptop_only.sh")()
    sh.cp([i3_laptop_config, i3_config])

elif set(edid_list) == set(docking_station + LVDS):
    mode = "docking"
    sh.Command(homedir+"bin/ScreenSwitcher/docking.sh")()
    sh.cp([ i3_docking_config, i3_config])

else:
    mode = "unknown"
    print("Please configure manually!")
    exit(0)

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


