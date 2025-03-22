@echo off
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Es werden administrative Rechte angefordert...
    powershell -Command "Start-Process '%~f0' -Verb runAs"
    exit /b
)
pushd %~dp0
python "health.py"

popd
pause
