from setuptools import setup, find_packages

setup(
    name="Quail",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    py_modules=["main"],
    install_requires=["click", "rich", "pytest"],

    entry_points={"console_scripts": ["Quail = cli.main:cli"]},
)