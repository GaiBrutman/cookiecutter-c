project(
  '{{ cookiecutter.project_slug }}',
  'c',
  version: '{{ cookiecutter.version }}',
  meson_version: '>=1.1.0',
  default_options: ['buildtype=release', 'warning_level=3'],
  license: '{{ cookiecutter.license }}',
)

project_headers = include_directories('include')
{% if cookiecutter.project_type == 'Library' -%}
project_source_files = [
  'src/{{ cookiecutter.project_slug }}.c',
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
project_dep = declare_dependency(
  include_directories: project_headers,
  objects: project_target.extract_objects(project_source_files),
)

if not meson.is_subproject()
  subdir('tests')

  test(
    'test_sanity',
    executable(
      'test_sanity',
      ['tests/test_sanity.c'],
      dependencies: [project_dep, test_dep],
      install: false,
    ),
  )
endif