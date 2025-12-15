@echo off
setlocal EnableDelayedExpansion

echo 🎨 Palette Pre-build Check...

set "CWD=%CD%"

:: 1. Check for spaces in path
echo "%CWD%" | find " " > nul
if %errorlevel% equ 0 (
    echo.
    echo ❌ ERROR: Space detected in project path:
    echo    %CWD%
    echo    The build tools may fail if the path contains spaces.
    echo    Please move the project to a path without spaces (e.g., C:\WRK).
    echo.
    echo ⚠️  WARNING: Continuing despite spaces in path. Build failures expected.
)

echo.
echo 📂 Working in: %CWD%
echo    Creating build directories...

set /a dir_count=0

:: Create dirs in build folders
:: Walk all subdirectories named "BUILD"
for /d /r . %%d in (BUILD) do (
    if exist "%%d" (
        set "target_root=%%d"

        :: Check/Create OBJI386
        if not exist "!target_root!\OBJI386" (
            mkdir "!target_root!\OBJI386"
            set /a dir_count=dir_count+1
        )

        :: Check/Create OBJAMD64
        if not exist "!target_root!\OBJAMD64" (
            mkdir "!target_root!\OBJAMD64"
            set /a dir_count=dir_count+1
        )
    )
)

:: Define specific directories to create
set "SPECIFIC_DIRS=WRK-V1.2\BASE\NTOS\BUILD\EXE ProjectOZ\BasicOZ\OBJI386 ProjectOZ\SPACE\OBJI386 ProjectOZ\runx86 ProjectOZ\files\i386"

for %%p in (%SPECIFIC_DIRS%) do (
    set "full_path=%CWD%\%%p"
    if not exist "!full_path!" (
        mkdir "!full_path!"
        set /a dir_count=dir_count+1
    )
)

if %dir_count% gtr 0 (
    echo.
    echo ✅ Done! Created %dir_count% missing directories.
) else (
    echo.
    echo ✅ Done! All directories already verified.
)

echo    You are ready to build WRK and ProjectOZ.

endlocal
