import subprocess 
import os

folder_path = os.getcwd()
print(folder_path)

script = f"ipynb-py-convert {folder_path}/Ziua2/exercitiu_numpy.py {folder_path}/Ziua2/exercitiu_numpy_3.ipynb"

subprocess.Popen(script, shell = True)