import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TheLegacyE", # Replace with your own username
    version="0.0.1",
    author="Mazi",
    author_email="mfetu1@mor123.com",
    description="Kelechi made me do this. :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheLegacyE/package-tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)