from setuptools import setup, find_packages

setup(
    name="libra",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "python-magic",
        "PyPDF2",
        "ebooklib",
    ],
    entry_points={
        "console_scripts": [
            "libra=libra.main:main",
        ],
    },
)
