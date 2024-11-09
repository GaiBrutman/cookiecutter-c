project(
  '{{ cookiecutter.project_slug }}',
  'c',
  version: '{{ cookiecutter.version }}',
  meson_version: '>=0.50.0',
  default_options: ['buildtype=release', 'warning_level=1'],
  license: '{{ cookiecutter.license }}',
)

# Source files to link with the unit tests.
source_files = []

project_headers = include_directories('include')
project_test_files = ['tests/test_sanity.c']

{% if cookiecutter.project_type == 'Library' -%}
project_source_files = [
  'src/{{ cookiecuttr.project_slug }}.c',
]

project_target = library(
  meson.project_name(),
  project_source_files,
  include_directories: project_headers,
  install: true,
)

{% elif cookiecutter.project_type == 'Executable' %}
# Exclude the main source file to link other objects with unit tests.
project_source_files = []

project_target = executable(
  meson.project_name(),
  project_source_files + ['src/main.c'],
  include_directories: project_headers,
)
{% endif %}

# Make objects usable as a static library.
# Make objects usable as a static library.
project_dep = declare_dependency(
  include_directories: project_headers,
  objects: project_target.extract_objects(source_files),
)

if not meson.is_subproject()
  subdir('tests')

  test(
    'test_sanity',
    executable(
      'test_sanity',
      files('tests/test_sanity.c'),
      dependencies: [project_dep, test_dep],
      install: false,
    ),
  )
endif