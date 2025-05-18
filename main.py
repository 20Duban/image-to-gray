import cv2
import pathlib
import matplotlib
import matplotlib.pyplot as plt

from os import listdir
from time import sleep

matplotlib.use("TKAgg")

def main():
    input_path = pathlib.Path("images")
    output_path = pathlib.Path("gray_images")
    
    if  not (input_path.exists() and output_path.exists()):
        print("❌ Error: make sure that the files images and gray_images exist in the root of the project")
        sleep(1)
        return

    file_names: list[str] = listdir(input_path)
    for file_name in file_names:
        try:
            
            image = cv2.imread(str(input_path/file_name))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            output_name: str = f"gray_{file_name}"
            cv2.imwrite(str(output_path/output_name), image)

        except Exception as _e:
            print(f"❌ Error: that file is not an valid image: {file_name}")

if __name__ == "__main__":
    main()
