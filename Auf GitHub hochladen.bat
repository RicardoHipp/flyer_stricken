@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Auf GitHub hochladen

where git >nul 2>&1
if errorlevel 1 (
    echo.
    echo   FEHLER: Git wurde nicht gefunden.
    echo   Von git-scm.com installieren.
    echo.
    pause
    exit /b 1
)

echo.
echo   ============================================
echo    Aenderungen auf GitHub hochladen
echo   ============================================
echo.

REM --- 1. Erzeugte Dateien auffrischen, damit nichts Veraltetes hochgeht ---
set PY=
where python >nul 2>&1 && set PY=python
if not defined PY where py >nul 2>&1 && set PY=py
if defined PY (
    echo   Erzeugte Dateien werden aufgefrischt ...
    %PY% tools\embed-assets.py
    echo.
) else (
    echo   Hinweis: Python nicht gefunden - assets.css, bg-data.js und
    echo   fonts-pdf.js werden NICHT aufgefrischt.
    echo.
)

REM --- 2. Gibt es ueberhaupt etwas zu tun? ---
set GEAENDERT=
for /f "delims=" %%i in ('git status --porcelain') do set GEAENDERT=ja
if not defined GEAENDERT (
    echo   Nichts geaendert - es gibt nichts hochzuladen.
    echo.
    pause
    exit /b 0
)

echo   Diese Dateien sind betroffen:
echo.
git status --short
echo.

REM --- 3. Beschreibung erfragen ---
set "MSG="
set /p "MSG=  Was hast du geaendert? (Enter = ohne Text): "
if not defined MSG set "MSG=Aktualisierung vom %DATE%"

echo.
git add -A
git commit -m "%MSG%"
if errorlevel 1 (
    echo.
    echo   Der Commit hat nicht geklappt - Meldung oben lesen.
    echo.
    pause
    exit /b 1
)

echo.
echo   Wird hochgeladen ...
git push
if errorlevel 1 (
    echo.
    echo   Das Hochladen hat nicht geklappt.
    echo   Haeufigster Grund: auf GitHub liegt etwas Neueres, weil dort
    echo   direkt im Browser geaendert wurde. Dann zuerst holen:
    echo.
    echo       git pull --rebase
    echo.
    echo   und die .bat danach nochmal starten. Der Commit ist schon
    echo   gespeichert, der geht nicht verloren.
    echo.
    pause
    exit /b 1
)

echo.
echo   Fertig. Die Seite zieht in ein bis zwei Minuten nach:
echo   https://ricardohipp.github.io/flyer_stricken/
echo.
pause
