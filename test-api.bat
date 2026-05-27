@echo off
REM Quick test script for AI Social Automation API
REM Make sure MongoDB is running and the server is started with: npm run dev

echo.
echo =====================================
echo AI Social Automation API Test Suite
echo =====================================
echo.

setlocal enabledelayedexpansion
set BASE_URL=http://localhost:5000/api
set TOKEN=

echo [1/5] Testing Health Check...
curl -s %BASE_URL:api=%health | findstr /C:"OK" >nul
if %errorlevel%==0 (
  echo ✅ Health check passed
) else (
  echo ❌ Health check failed - Is the server running?
  exit /b 1
)

echo.
echo [2/5] Testing User Registration...
for /f "tokens=*" %%A in ('curl -s -X POST %BASE_URL%/auth/register -H "Content-Type: application/json" -d "{\"name\":\"Test User\",\"email\":\"test@example.com\",\"password\":\"TestPass123\",\"confirmPassword\":\"TestPass123\"}" ^| findstr "token"') do set TOKEN=%%A

if not "!TOKEN!"=="" (
  echo ✅ Registration successful
  REM Extract token (basic parsing)
  for /f "tokens=2 delims=:," %%B in ("!TOKEN!") do set TOKEN=%%B
  set TOKEN=!TOKEN:"=!
  set TOKEN=!TOKEN: =!
  echo Token received (length: !TOKEN:~0,20!...)
) else (
  echo ❌ Registration failed
  exit /b 1
)

echo.
echo [3/5] Testing User Login...
curl -s -X POST %BASE_URL%/auth/login -H "Content-Type: application/json" -d "{\"email\":\"test@example.com\",\"password\":\"TestPass123\"}" | findstr /C:"token" >nul
if %errorlevel%==0 (
  echo ✅ Login successful
) else (
  echo ❌ Login failed
)

echo.
echo [4/5] Testing Create Post...
if not "!TOKEN!"=="" (
  curl -s -X POST %BASE_URL%/posts -H "Content-Type: application/json" -H "Authorization: Bearer !TOKEN!" -d "{\"content\":\"Test post\",\"platforms\":[\"twitter\",\"facebook\"]}" | findstr /C:"success" >nul
  if !errorlevel!==0 (
    echo ✅ Create post successful
  ) else (
    echo ❌ Create post failed
  )
) else (
  echo ⚠️  Skipping post creation (no valid token)
)

echo.
echo [5/5] Testing Get Posts...
if not "!TOKEN!"=="" (
  curl -s -X GET %BASE_URL%/posts -H "Authorization: Bearer !TOKEN!" | findstr /C:"success" >nul
  if !errorlevel!==0 (
    echo ✅ Get posts successful
  ) else (
    echo ❌ Get posts failed
  )
) else (
  echo ⚠️  Skipping get posts (no valid token)
)

echo.
echo =====================================
echo ✅ Test suite completed!
echo =====================================
echo.
echo API Endpoints:
echo - POST   /api/auth/register  - Register new user
echo - POST   /api/auth/login     - Login user
echo - GET    /api/auth/me        - Get current user
echo - POST   /api/auth/logout    - Logout user
echo - GET    /api/posts          - List all posts
echo - POST   /api/posts          - Create new post
echo - GET    /api/posts/:id      - Get single post
echo - PUT    /api/posts/:id      - Update post
echo - DELETE /api/posts/:id      - Delete post
echo - POST   /api/posts/:id/publish - Publish post
echo.
echo For more details, see API_DOCS.md
echo.
pause
