from pathlib import Path
from setuptools import setup

here = Path(__file__).parent

about = {}
exec((here / "esphome_extras/__version__.py").read_text(), about)

setup(version=about["__version__"])
