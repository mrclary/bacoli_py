for %%i in (%RECIPE_DIR%\..\dist\bacoli*.whl) do (
    set "wheel_path=%%~fi"
)
%PYTHON% -m pip install --no-deps %wheel_path%
