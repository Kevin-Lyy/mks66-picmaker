filename = "Macrohard.ppm"
file = open(filename,"w+")
file.write("P3 500 500 255\n")

for x in range(500):
    for y in range(500):
        if x < 250 and y < 250:
            file.write("255 75 20 ")
        elif x < 250 and y > 250:
            file.write("102 204 0 ")
        elif x > 250 and y < 250:
            file.write("102 178 255 ")
        elif x > 250 and y > 250:
            file.write("235 176 40 ")
        else:
            file.write("0 0 0 ")

file.close()
