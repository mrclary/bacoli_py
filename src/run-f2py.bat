@echo off

@rem This script is required because f2py will only save the output compiled
@rem file to the current directory, but meson expects it to be in src

set "python=%~1"
set "out_dir=%~dp2"
set "out_file=%~nx2"
shift /2

set "fortran_files=%~2" & shift
:loop
if not "%~2"=="" set "fortran_files=%fortran_files% %~2" & shift & goto :loop

@echo on

"%python%" -m numpy.f2py --backend meson -m bacoli_interface -c %fortran_files%

move %out_file% "%out_dir%"
