from setuptools import setup, find_packages

setup(
    name="car-analyzer",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests",
        "beautifulsoup4", 
        "pandas",
        "typer",
        "rich"
    ]
)