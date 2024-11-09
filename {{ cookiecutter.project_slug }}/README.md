# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Structure

```txt
src/                    All .c files
include/                All .h files. Used as "#include {{ cookiecutter.project_slug }}/header.h"
    {{ cookiecutter.project_slug }}/
tests/                  All test files
build/                  Build directory (gitignored)
conanfile.py            Conan package file
meson.build             Meson build file
requirements.txt        Python requirements
.gitignore              Git ignore file
README.md               This file
.clang-format           Clang formatting options
.pre-commit-config.yaml Pre-commit configuration
```

## Dependencies

- [meson](https://mesonbuild.com/) for building.
- [ninja](https://ninja-build.org/) for building.
- [conan](https://conan.io/) for package management.
- [Unity](https://www.throwtheswitch.org/unity) for testing.

### Building

```bash
conan build .
```

### Testing

The Unity test framework is used for unit testing.

```bash
conan test . {{ cookiecutter.project_slug }}/latest
```

### VSCode Integration

Open {{ cookiecutter.project_slug }}.code-workspace in VSCode
