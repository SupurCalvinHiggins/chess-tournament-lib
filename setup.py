import setuptools

setuptools.setup(
      name="chess tournament",
      version="0.1",
      description="Some utilities for simple chess tournaments with the python-chess package.",
      author="Calvin Higgins",
      author_email="calvin_higgins2@uri.edu",
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      python_requires=">=3.9",
      install_requires=["python-chess", "pytest"],
)