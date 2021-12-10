from setuptools import setup, find_packages

setup(
    name="hexgrid-group",
    extras_require={
        "dev": ["pytest", "mypy", "black", "flake8", "isort"],
    },
    packages=find_packages(exclude=["tests"]),
    package_data={
        package: ["py.typed"] for package in find_packages(exclude=["tests"])
    },
)
