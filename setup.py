from skbuild import setup

setup(
    name="heongpu_py",
    version="1.2.3",
    description="a minimal example package (cpp version)",
    author='The scikit-build team',
    license="MIT",
    package_dir={"heongpu_py": "src/heongpu_py"},
    packages=['heongpu_py'],
    python_requires=">=3.8",
)

