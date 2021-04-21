import setuptools

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="facebook",
    version="1.0.0",
    author="Haithem FRAD",
    author_email="fhaithe",
    license="MIT",
    description="Facebook scrapping service using fastAPI",
    long_description_content_type="text/markdown",
    # long_description=readme,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=["selenium==3.141.0", "webdriver_manager"])