import os
   
image_ids_folder = set()
from os import listdir

folder_dir = "/Users/ledrithaqi/Desktop/UZH/Master Thesis/VQG_RaD/Dataset/imgs"

#for images in os.listdir(folder_dir):
 #   if(images.endswith(".jpg")):
  #      image_ids_folder.add(images)
   #     print(image_ids_folder)

"""
for directory in os.listdir(folder_dir):
    for images in directory:
        if(images.endswith("source.jpg")):
            image_ids_folder.add(images)
            print(image_ids_folder)
"""
import os
for root, dirs, files in os.walk("/Users/ledrithaqi/Desktop/UZH/Master Thesis/VQG_RaD/Dataset/imgs"):
    for fname in files:
        if fname.endswith(".jpg"):
            fpath = os.path.join(root, fname)
            image_ids_folder.add(fpath)
            print(image_ids_folder)


