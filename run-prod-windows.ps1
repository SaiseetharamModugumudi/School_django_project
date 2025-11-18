<#
Run production-like server on Windows using Waitress (WSGI).

Usage (PowerShell):
  1. Open PowerShell in the project root (`D:\Django\School`).
  2. Optionally allow script execution for this session:
       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  3. Run this script:
       .\run-prod-windows.ps1

This script will:
  - create a `.venv` virtual environment if it doesn't exist
  - activate the venv
  - upgrade pip/setuptools/wheel
  - install `waitress`
  - run the app using `python -m waitress` on port 8000

#>

function Abort($msg) {
    Write-Error $msg
    exit 1
}

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Abort "Python not found. Install Python 3.8+ and ensure `python` is on PATH." 
}

$venvPath = Join-Path $PSScriptRoot '.venv'
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at $venvPath..."
    python -m venv .venv || Abort "Failed to create virtual environment."
} else {
    Write-Host "Using existing virtual environment at $venvPath"
}

Write-Host "Activating virtual environment..."
try {
    . $venvPath\Scripts\Activate.ps1
} catch {
    Write-Warning "Could not activate automatically. Try running: .\$venvPath\Scripts\Activate.ps1"
}

Write-Host "Upgrading pip, setuptools and wheel..."
python -m pip install --upgrade pip setuptools wheel

Write-Host "Installing Waitress (WSGI server supported on Windows)..."
python -m pip install waitress

Write-Host "Starting Waitress on port 8000 (press Ctrl+C to stop)..."
# Use the module runner so the console entrypoint is not required on PATH
python -m waitress --port=8000 School.wsgi:application
