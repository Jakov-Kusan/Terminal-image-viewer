print("loading colors ",end="")
class color:
    red = '\033[91m'
    yellow = '\033[93m'
    green = '\033[92m'

    none = '\033[0m'
print(color.green + "[done]" + color.none)


print("importing modules ",end="")
try:
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
except:
    print(color.red + "[ERROR]"+color.none)
    exit()

print(color.green + "[done]" + color.none)

print("declaring functions ",end="")
def printrgb(r, g, b, text):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m",end="")
print(color.green + "[done]" + color.none)


imageName = input("Name of image? ")
print("loading", imageName+" ",end = "")

try:
    image=mpimg.imread(imageName)
except:
    print(color.red + "[ERROR]"+color.none)
    exit()

print(color.green + "[done]" + color.none)
print("array lenght",len(image))

for i in range(len(image)):
    print("")
    for j in range(len(image[i])):
        printrgb(int(image[i][j][0]*255),int(image[i][j][1]*255),int(image[i][j][2]*255),"@")

print("")





