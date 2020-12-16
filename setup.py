from setuptools import setup, find_packages

setup(
    name="unet",
    version="0.0.1",
    author='Jiyeon Baek',
    author_email="whitedelay@gmail.com",
    url="https://github.com/skku-capstone-2020-fall-group13/UNet.git",
    install_requires= [
        "torchvision>=0.7.0",
        "numpy==1.19.2",
        "segmentation-models-pytorch==0.1.2",
        "scikit-learn>=0.23",
        "tqdm==4.49.0",
    ],
    description="Unet for image segmentation",
    packages=find_packages()
)