"""_summary_
"""

from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="Conversor de Unidades",
    version="0.0.1",
    author="Daniel Torres de Andrade",
    author_email="danieltorresandrade@gmail.com",
    description="Este projeto é de um conversor simples de unidades.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Danieltandrade/Unit-Converter",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)
