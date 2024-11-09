project(
  '{{ cookiecutter.project_slug }}',
  'c',
  version: '{{ cookiecutter.version }}',
  meson_version: '>=0.50.0',
  default_options: ['buildtype=release', 'warning_level=1'],
  license: '{{ cookiecutter.license }}',
)

project_headers = include_directories('include')
project_source_files = ['src/{{ cookiecutter.project_slug }}.c']
project_test_files = ['tests/test_sanity.c']

project_target = library(
  meson.project_name(),
  project_source_files,
  include_directories: project_headers,
  install: true,
)

# Make this library usable as a Meson subproject.
project_dep = declare_dependency(
  include_directories: project_headers,
  link_with: project_target,
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