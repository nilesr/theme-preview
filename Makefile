all:
	echo "Did you change the number of images in the makefile from 901?"
	png2yuv -I p -f 20 -b 0 -n 901 -j '%03d-b.png' > test.yuv
	vpxenc --good --cpu-used=0 --auto-alt-ref=1 --lag-in-frames=16 --end-usage=vbr --passes=2 --threads=2 --target-bitrate=3000 -o vpxenc --good --cpu-used=0 --auto-alt-ref=1 --lag-in-frames=16 --end-usage=vbr --passes=2 --threads=2 --target-bitrate=3000 -o test.webm test.yuv
