filename = "file.ppm"
file = open(filename,"w+")
file.write("P3 500 500 255\n")

for c in range(500):
    for c in range(250):
        file.write("255 75 20 ")

for c2 in range(500):
    for i2 in range(500):
        file.write("235 176 40 ")

#235 105 40
#102 204 0
#102 178 255
#235 176 40

file.close()
