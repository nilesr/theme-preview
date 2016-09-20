import glob, subprocess
f = glob.glob("*.png")
f.sort()
for i in range(len(f)):
    thisfile = f[i]
    subprocess.call(["mv", thisfile, str(i).rjust(3, "0") + ".png"])
