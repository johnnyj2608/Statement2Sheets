import os
import pandas as pd

def parseMetadata(file, imgDir):
    data = []
    with open(file, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                parts = line.strip().split(' ')
                imageID = parts[0]
                
                imageParts = imageID.split('-')
                folder = imageParts[0]
                subfolder = '-'.join(imageParts[:2])
                imagePath = os.path.join(imgDir, folder, subfolder, f"{imageID}.png")

                text = ' '.join(parts[8:]).replace('|', ' ')
                data.append((imagePath, text))
    return pd.DataFrame(data, columns=["imagePath", "text"])

file = "trainingData\lines.txt"
imgDir = "trainingData"
data = parseMetadata(file, imgDir)
print(data.head())