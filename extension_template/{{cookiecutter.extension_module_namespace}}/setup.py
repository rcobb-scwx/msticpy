from setuptools import setup, find_namespace_packages
from pathlib import Path

requirements = [
    requirement 
    for requirement in Path("requirements.txt").read_text().splitlines() 
    if requirement
]

setup(
    name="{{cookiecutter.extension_module_reference}}",
    author="{{cookiecutter.author_name}}",
    description="{{cookiecutter.extension_description}}",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    version="0.1a",
    packages=find_namespace_packages(),
    namespace_packages=["msticpy_extensions"],
     package_data={"msticpy_extensions.{{cookiecutter.extension_module_reference}}.queries": ["*.yaml"]},
    python_requires="{{cookiecutter.python_min_version_required}}",
    install_requires=requirements,
)
