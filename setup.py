from pathlib import Path

from setuptools import find_packages, setup

extras_requires = {
    "dev_docs": ["recommonmark", "sphinx_rtd_theme", "sphinx-autodoc-typehints"],
    "dev_compile": ["Cython", "pandas"],
}

tests_require = ["pytest"]

source_root = Path(".")
with (source_root / "README.md").open(encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tangled_up_in_unicode",
    version="0.2.0",
    description="Access to the Unicode Character Database (UCD)",
    url="https://github.com/dylan-profiler/tangled-up-in-unicode",
    license="BSD License",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    include_package_data=True,
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
    ],
)
