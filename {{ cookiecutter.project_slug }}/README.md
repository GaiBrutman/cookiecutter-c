# c-template

A C project cookiecutter

## Library

Using meson for compilation and conan for library managment.

### Structure

src/                All .c files
include/
    {{ cookiecutter.project_slug }}  All .h files. Uses as "#include {{ cookiecutter.project_slug }}/header.h"

### Dependencies

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
