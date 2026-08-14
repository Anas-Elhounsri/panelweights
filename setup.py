from setuptools import setup, find_packages

setup(
    name="panelweights",
    version="0.6.0",
    description="Design weights and non-response adjustment for household panels",
    author="Ines Duarte",
    author_email="ines.duarte@example.org",
    packages=find_packages(),
    install_requires=["pandas>=2.0.0", "numpy>=1.24.0"],
)
