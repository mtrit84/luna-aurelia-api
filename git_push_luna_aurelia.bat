@echo off
echo ====================================
echo   Luna Aurelia - GitHub Push Helper
echo ====================================

:: Ask for user input
set /p GIT_USER=GitHub Benutzername:
set /p GIT_REPO=Repository Name (z.B. luna-aurelia-api):

:: Configure git user (optional)
git config --global user.name "Luna Aurelia User"
git config --global user.email "luna@example.com"

:: Initialize git repo if needed
if not exist .git (
    git init
)

:: Add remote if needed
git remote add origin https://github.com/%GIT_USER%/%GIT_REPO%.git 2>nul

:: Stage and commit
git add .
git commit -m "Deploy Luna Aurelia API"

:: Push to GitHub
git push -u origin master

pause