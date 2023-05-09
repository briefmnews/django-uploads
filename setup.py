from setuptools import setup

from uploads import __version__

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-uploads",
    version=__version__,
    description="Django simple file uploader app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/briefmnews/django-uploads",
    author="Brief.me",
    author_email="tech@brief.me",
    license="MIT",
    packages=["uploads", "uploads.signals", "uploads.migrations"],
    python_requires=">=3.6",
    install_requires=[
        "Django>=3",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    zip_safe=False,
)
