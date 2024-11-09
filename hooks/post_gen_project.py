#!/usr/bin/env python
import pathlib

if __name__ == "__main__":
    if "Not open source" == "{{ cookiecutter.license }}":
        pathlib.Path("LICENSE").unlink()

    if "Library" != "{{ cookiecutter.project_type }}":
        pathlib.Path("src/{{ cookiecutter.project_slug }}.c").unlink()
    elif "Executable" != "{{ cookiecutter.project_type }}":
        pathlib.Path("src/main.c").unlink()
