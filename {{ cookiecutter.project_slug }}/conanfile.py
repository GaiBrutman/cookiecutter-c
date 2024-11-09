from pathlib import Path
import re
from conan import ConanFile
from conan.tools.meson import Meson
from conan.tools.layout import basic_layout


def get_project_option_from_meson(option: str) -> str:
    return re.search(
        rf"\s*{option}\s*:\s*\'(.*)\'", Path("meson.build").read_text()
    ).group(1)


class PkgConan(ConanFile):
    name = "{{ cookiecutter.project_slug }}"
    version = get_project_option_from_meson("version")
    license = get_project_option_from_meson("license")

    requires = ["unity/2.6.0"]

    generators = ["PkgConfigDeps", "MesonToolchain"]
    settings = ["os", "compiler", "arch"]

    def layout(self):
        basic_layout(self)

    def build(self):
        meson = Meson(self)
        meson.configure()
        meson.build()

    def test(self):
        meson = Meson(self)
        meson.test()

    def package(self):
        meson = Meson(self)
        meson.install()
