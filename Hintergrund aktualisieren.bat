@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo.
echo   Baut assets.css und fonts-pdf.js aus Hintergrund.jpg neu.
echo.

if not exist "Hintergrund.jpg" (
    echo   FEHLER: Hintergrund.jpg liegt nicht in diesem Ordner.
    echo.
    pause
    exit /b 1
)

set PY=
where python >nul 2>&1 && set PY=python
if not defined PY where py >nul 2>&1 && set PY=py
if not defined PY (
    echo   FEHLER: Python wurde nicht gefunden.
    echo   Von python.org installieren und dabei "Add to PATH" ankreuzen.
    echo.
    pause
    exit /b 1
)

%PY% tools\embed-assets.py
if errorlevel 1 (
    echo.
    echo   Das hat nicht geklappt - Meldung oben lesen.
    echo.
    pause
    exit /b 1
)

echo.
echo   Fertig. Jetzt index.html neu laden (Strg+F5).
echo.
pause
