@echo off
REM Create directory structure for AI Social Media Automation project

cd /d C:\Users\SADANAND\ai-social-automation

echo Creating directories...
mkdir src
mkdir src\config
mkdir src\middleware
mkdir src\controllers
mkdir src\routes
mkdir src\services
mkdir src\models
mkdir src\utils
mkdir tests

echo.
echo ✅ Directories created successfully!
echo.
echo Project structure created in: C:\Users\SADANAND\ai-social-automation
echo.
echo Next steps:
echo 1. cd C:\Users\SADANAND\ai-social-automation
echo 2. npm install
echo 3. cp .env.example .env
echo 4. npm run dev (for development)
echo.
pause
