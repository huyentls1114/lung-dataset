import os
import glob
import shutil

class CovidChestXray:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        self.init_name()
    def init_name(self):
        self.image_folder = os.path.join(self.input_folder, "images")
        self.mask_folder = os.path.join(self.input_folder, "annotations/lungVAE-masks")
        self.list_mask_names = os.listdir(self.mask_folder)
        self.list_img_names = list(x.replace(".png", ".jpg") for x in self.list_mask_names)
        

    