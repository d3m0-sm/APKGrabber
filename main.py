from os import popen as cmd
import platform
import sys
grep = "grep"
plat = platform.system()
if plat == "Windows":
    grep = "findstr"
try:
    cmd("adb devices")
except:
    print("Fatal Error: ADB is not installed")
    sys.exit()
data_path = ""
app = "9"
result_path = f"/home/$USER/Downloads/"
if plat == "Windows":
    result_path = f"C:\\Users\\%username%\\Downloads\\"
ac = cmd("adb devices")
devices = ac.read().replace("List of devices attached", "")
if "device" not in devices:
    print("No device connected!")
    sys.exit()
else:
    print("Device found\n")
while app not in data_path:
    app = input("Please specify which application do you want to dump: ")
    pm = cmd(f"adb shell pm list packages -f | {grep} {app}")
    data_path = pm.read().replace("package:", "").split(".apk")
    data_path = data_path[0] + ".apk"
    if app not in data_path:
        print("App not found try again")
        print("Hint: maybe try the publisher or developer\n")

cmd(f"adb pull {data_path} {result_path}{app}.apk")
print("APK successfully stored in Downloads directory")
