import glob
import PIL.Image
for f in glob.glob("*-a.png"):
    old = PIL.Image.open(f)
    new = PIL.Image.new("RGB", (500, 250), (0, 0, 0))
    for x in range(old.width):
        for y in range(old.height):
            try:
                new.putpixel((int(500/2) + x - int(old.width / 2), int(250/2) + y - int(old.height / 2)), old.getpixel((x, y)))
            except:
                pass
    new.save(f.replace("-a.png", "-b.png"))
    print(f)
