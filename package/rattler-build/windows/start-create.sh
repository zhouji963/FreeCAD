#!/bin/bash

# 1. 加载环境变量
export BUILD_TAG="1.2.0Dev"
export NUMBER_OF_PROCESSORS="8"
export MAKE_INSTALLER="true"
export UPLOAD_RELEASE="false"
export WINDOWS_SIGN_RELEASE="0"
# 把 NSIS_INSTALL 设置为 NSIS 的【上级目录】
export NSIS_INSTALL="D:/Program Files/NSIS"
echo "============================================="
echo "        FreeCAD Windows 打包一键启动"
echo "============================================="
echo "版本号:      $BUILD_TAG"
echo "CPU核心数:   $NUMBER_OF_PROCESSORS"
echo "生成安装包:  $MAKE_INSTALLER"
echo "上传Release: $UPLOAD_RELEASE"
echo "Azure签名:   $WINDOWS_SIGN_RELEASE"
echo "NSIS安装位置: $NSIS_INSTALL"
echo "============================================="
sleep 2

# 2. 给打包脚本加执行权限（防止权限不足）
chmod +x create_bundle.sh

# 3. 自动执行打包脚本
echo "开始执行打包脚本..."
./create_bundle.sh

echo "============================================="
echo "打包流程执行完毕！"
echo "============================================="
read -p "按回车键关闭窗口..."