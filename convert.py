import glob
import PIL.Image
fw = 500
fh = 250
for f in glob.glob("*-a.png"):
    old = PIL.Image.open(f)
    new = PIL.Image.new("RGB", (fw, fh), (0, 0, 0))
    for x in range(old.width):
        for y in range(old.height):
            try:
                new.putpixel((int(fw/2) + x - int(old.width / 2), int(fh/2) + y - int(old.height / 2)), old.getpixel((x, y)))
            except:
                pass
    new.save(f.replace("-a.png", "-b.png"))
    print(f)
