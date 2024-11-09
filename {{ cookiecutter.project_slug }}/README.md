# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

Using meson for compilation and conan for library management.

## Structure

```txt
src/                    All .c files
include/                All .h files. Used as "#include {{ cookiecutter.project_slug }}/header.h"
    {{ cookiecutter.project_slug }}/
tests/                  All test files
build/                  Build directory
conanfile.txt           Conan dependencies
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
conan install . --output-folder=build --build=missing # Install dependencies
meson setup --native-file build/conan_meson_native.ini build
meson compile -C build/
```

### Testing

The Unity test framework is used for unit testing.

```bash
meson test -C build/
```

### VSCode Integration

Open {{ cookiecutter.project_slug }}.code-workspace in VSCode
