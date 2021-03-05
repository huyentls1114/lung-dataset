import os
import glob
import shutil

class CovidChestXray:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        self.init_name()
        self.init_output()
    def init_name(self):
        self.image_folder = os.path.join(self.input_folder, "images")
        self.mask_folder = os.path.join(self.input_folder, "annotations/lungVAE-masks")
        self.list_mask_names = os.listdir(self.mask_folder)
    def init_output(self):
        self.output_image_folder = os.path.join(self.output_folder, "images")
        self.output_mask_folder = os.path.join(self.output_folder, "masks")
        if not os.path.isdir(self.output_image_folder):
            os.makedirs(self.output_image_folder)
        if not os.path.isdir(self.output_mask_folder):
            os.makedirs(self.output_mask_folder)

    def copy_images(self):
        self.list_img_name = []
        for mask_name in self.list_mask_names:
            try:
                img_name = mask_name.replace("_mask.png", ".jpg")
                img_path = os.path.join(self.image_folder, mask_name)
                mask_path = os.path.join(self.mask_folder, mask_name)
                img_path_output = os.path.join(self.output_image_folder, img_name)
                mask_path_output = os.path.join(self.output_mask_folder, img_name)
                shutil.copy(img_path, img_path_output)
                shutil.copy(mask_path, mask_path_output)
                self.list_img_name.append(img_name)
            except Exception as e:
                print(e)