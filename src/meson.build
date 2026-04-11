python = import('python').find_installation()

fortran_sources = files(
    'lib/bacoli_interface.pyf',
    'lib/bacoli_interface.f95',
    'lib/bacoli.f',
    'lib/bacoli-aux.f',
    'lib/d1mach_i1mach.f95',
    'lib/bacolri.f',
    'lib/bacolri-aux.f'
)

# Handle fixed-form Fortran (.f files)
add_project_arguments('-ffixed-form', language: 'fortran')

pkg_dir = join_paths(python.get_install_dir(), 'bacoli_py')

# Determine platform suffix
bacoli_so = 'bacoli_interface' + run_command(
    python,
    '-c',
    'import sysconfig; print(sysconfig.get_config_var("EXT_SUFFIX"))',
    check: true
).stdout().strip()

# Build extension via f2py
f2py_module = custom_target(
    'bacoli_interface_module',
    input: fortran_sources,
    output: bacoli_so,
    command: [
        python, '-m', 'numpy.f2py',
        '-c',
        '-m', 'bacoli_interface',
        '@INPUT@',
        '&&', 'mv', bacoli_so, 'src/'
    ],
    install: true,
    install_dir: pkg_dir,
    install_tag: 'runtime'
)

# Install Python sources
python.install_sources(
    [
        'bacoli_py/__init__.py',
        'bacoli_py/Evaluation.py',
        'bacoli_py/ProblemDefinition.py',
        'bacoli_py/Solver.py'
    ],
    subdir: 'bacoli_py'
)

# Install data files (licenses)
install_data(
    '../LICENSE.txt',
    'lib/BACOLI-LICENSE.txt',
    'lib/BACOLRI-LICENSE.txt',
    install_dir: pkg_dir,
    install_tag: 'license'
)
