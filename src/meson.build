python = import('python').find_installation()

fortran_sources = files(
    'lib/bacoli_interface.pyf',
    'lib/bacoli_interface.f95',
    'lib/bacoli.f',
    'lib/bacoli-aux.f',
    'lib/d1mach_i1mach.f95',
    'lib/bacolri.f',
    'lib/bacolri-aux.f',
)

pkg_dir = join_paths(python.get_install_dir(), 'bacoli_py')

script = 'run-f2py.sh'
if host_machine.system() == 'windows'
    script = 'run-f2py.bat'
endif

# Determine platform suffix
bacoli_mod_name = 'bacoli_interface' + run_command(
    python,
    '-c',
    'import sysconfig; print(sysconfig.get_config_var("EXT_SUFFIX"))',
    check: true,
).stdout().strip()

# Build extension via f2py
bacoli_mod = custom_target(
    'bacoli_interface',
    input: fortran_sources,
    output: bacoli_mod_name,
    command: [script, python, '@OUTPUT@', '@INPUT@'],
    install: true,
    install_dir: pkg_dir,
    install_tag: 'runtime',
)

# Install Python sources
python.install_sources(
    [
        'bacoli_py/__init__.py',
        'bacoli_py/Evaluation.py',
        'bacoli_py/ProblemDefinition.py',
        'bacoli_py/Solver.py'
    ],
    subdir: 'bacoli_py',
)
