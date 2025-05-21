pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'effective_screen_resolution_calculator'
gnome = import('gnome')

gnome.compile_resources('effective_screen_resolution_calculator',
  'effective_screen_resolution_calculator.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'effective_screen_resolution_calculator.in',
  output: 'effective_screen_resolution_calculator',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr-xr-x'
)

effective_screen_resolution_calculator_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]

install_data(effective_screen_resolution_calculator_sources, install_dir: moduledir)
