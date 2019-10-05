from setuptools import setup
from setuptools import find_packages


extras_requires = {
    "dev_docs": ["recommonmark", "sphinx_rtd_theme", "sphinx-autodoc-typehints"],
    "dev_compile": ["Cython", "pandas"],
}

tests_require = ["pytest"]
#
setup(
    name="tangled_up_in_unicode",
    version="0.0.3",
    description="Access to the Unicode Character Database (UCD)",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    include_package_data=True,
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
    ],
)
