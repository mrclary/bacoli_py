from pathlib import Path
import subprocess as sp
import sys
from tempfile import gettempdir


def f2py_compile(
    source: str, modulename: str = 'untitled', extra_args: [str|list] = "",
    verbose: bool = True, source_fn: [str|type(None)] = None,
    extension: str = ".f"
) -> sp.CompletedProcess:
    """
    Compile user Fortran code into module using f2py with meson backend.

    The command used is:
    `python -m numpy.f2py --backend meson -m MODULENAME -c source.f [EXTRA_ARGS]`

    Parameters
    ----------
    source : str
        Fortran source of module / subroutine to compile.
    modulename : str, optional
        The name of the compiled python module. The default is 'untitled'.
    extra_args : [str|list], optional
        Additional parameters passed to `f2py`. The default is "".
    verbose : bool, optional
        Print `f2py` output to screen. The default is True. If False, stdout and
        stderr are not captured by the CompletedProcess object.
    source_fn : [str|type(None)], optional
        Name of the file where the fortran source is written. The default is to
        use a temporary file with the extension provided by the `extension`
        parameter.
    extension : {".f", ".f90", "f.95"}, optional
        Filename extension if source_fn is not provided. The extension tells
        which fortran standard is used. The default is `.f`, which implies F77
        standard.

    Returns
    -------
    proc : CompletedProcess
        The subprocess used to compile the module.

    Raises
    ------
    CalledProcessError:
        Raised if process fails.
    """
    if source_fn:
        source_fn = Path(source_fn).resolve()
    elif source:
        if extension not in {".f", ".f90", ".f95"}:
            extension = ".f"
        source_fn = Path(gettempdir()) / f"source{extension}"
        source_fn.write_text(source, encoding="ascii")

    if not source_fn.exists():
        raise FileNotFoundError("Cannot find %s", source_fn)

    cmd = [
        sys.executable,
        "-m", "numpy.f2py",
        "--backend", "meson",
        "-m", modulename,
        "-c", str(source_fn)
    ]
    if extra_args:
        if isinstance(extra_args, str):
            cmd.append(extra_args)
        if isinstance(extra_args, list):
            cmd.extend(extra_args)

    proc = sp.run(cmd, capture_output=not verbose, check=True, text=True)

    return proc
