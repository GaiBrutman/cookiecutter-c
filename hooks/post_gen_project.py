#!/usr/bin/env python
import pathlib

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.license }}":
        pathlib.Path("LICENSE").unlink()

    if "Library" != "{{ cookiecutter.project_type }}":
        pathlib.Path("src/{{ cookiecutter.project_slug }}.c").unlink()
        pathlib.Path(
            "include/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.h"
        ).unlink()
    elif "Executable" != "{{ cookiecutter.project_type }}":
        pathlib.Path("src/main.c").unlink()
