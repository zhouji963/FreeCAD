@echo off
chcp 65001
echo ==============================================
echo  一键同步 FreeCAD 官方代码到自己仓库
echo ==============================================
echo.

:: 切换到 main 分支
git checkout main

:: 拉取官方仓库更新
git fetch upstream

:: 合并官方最新代码到本地main
git merge upstream/main

:: 推送到自己的 GitHub 仓库
git push origin main

echo.
echo ==============================================
echo  自己仓库、本地的main分支已与官方仓库同步完成！
echo ==============================================
pause