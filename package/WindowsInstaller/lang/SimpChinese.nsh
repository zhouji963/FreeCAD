/*
FreeCAD Installer Language File
Language: SimpChinese
*/

!insertmacro LANGFILE_EXT "SimpChinese"

${LangFileString} TEXT_INSTALL_CURRENTUSER "(为当前用户安装)"

${LangFileString} TEXT_WELCOME "这个向导将引导你安装 $(^NameDA). $\r$\n\
				$\r$\n\
				$_CLICK"

#${LangFileString} TEXT_CONFIGURE_PYTHON "编译 Python 脚本..."

${LangFileString} TEXT_FINISH_DESKTOP "创建桌面快捷方式"
${LangFileString} TEXT_FINISH_WEBSITE "访问 freecad.org/ 获取最新新闻、支持和技巧"

#${LangFileString} FileTypeTitle "FreeCAD文档"

#${LangFileString} SecAllUsersTitle "为所有用户安装?"
${LangFileString} SecFileAssocTitle "文件关联"
${LangFileString} SecDesktopTitle "桌面图标"

${LangFileString} SecCoreDescription "FreeCAD 文件."
#${LangFileString} SecAllUsersDescription "为所有用户还是仅当前用户安装 FreeCAD."
${LangFileString} SecFileAssocDescription "带有.FCStd后缀的文件将自动在 FreeCAD 中打开."
${LangFileString} SecDesktopDescription "在桌面上创建FreeCAD图标."
#${LangFileString} SecDictionaries "Dictionaries"
#${LangFileString} SecDictionariesDescription "可下载和安装的拼写检查词典."

#${LangFileString} PathName 'Path to the file $\"xxx.exe$\"'
#${LangFileString} InvalidFolder 'The file $\"xxx.exe$\" is not in the specified path.'

#${LangFileString} DictionariesFailed 'Download of dictionary for language $\"$R3$\" failed.'

#${LangFileString} ConfigInfo "以下 FreeCAD 配置可能需要一段时间."

#${LangFileString} RunConfigureFailed "无法运行配置脚本."
${LangFileString} InstallRunning "安装程序已经运行中!"
${LangFileString} AlreadyInstalled "FreeCAD ${APP_SERIES_KEY2} 已安装!$\r$\n\
				如果已安装版本是测试版，或者你现有的 FreeCAD 安装有问题，不建议在现有安装上安装。.$\r$\n\
				在这种情况下最好重新安装 FreeCAD.$\r$\n\
				你还要安装已存在的版本吗?"
${LangFileString} NewerInstalled "你正在尝试安装比你安装的版本更旧的 FreeCAD.$\r$\n\
				  如果你真的想要这个，必须先卸载现有的FreeCAD $OldVersionNumber ."

#${LangFileString} FinishPageMessage "恭喜！FreeCAD 已成功安装.$\r$\n\
#					$\r$\n\
#					(FreeCAD 的首次启动可能需要几秒钟.)"
${LangFileString} FinishPageRun "Launch FreeCAD"

${LangFileString} UnNotInRegistryLabel "无法在注册表中找到 FreeCAD.$\r$\n\
					桌面和开始菜单上的快捷方式不会被."
${LangFileString} UnInstallRunning "你必须先关闭 FreeCAD!"
${LangFileString} UnNotAdminLabel "卸载 FreeCAD 必须拥有管理员权限!"
${LangFileString} UnReallyRemoveLabel "你确定要完全移除 FreeCAD 及其所有组件吗?"
${LangFileString} UnFreeCADPreferencesTitle 'FreeCAD$\'s user preferences'

#${LangFileString} SecUnProgDescription "Uninstalls xxx."
${LangFileString} SecUnPreferencesDescription '删除 FreeCAD$\'s 配置$\r$\n\
						(目录 $\"$AppPre\username\$\r$\n\
						$AppSuff\$\r$\n\
						${APP_DIR_USERDATA}$\")$\r$\n\
						为你或所有用户（如果你是管理员）.'
${LangFileString} DialogUnPreferences '你选择删除了 FreeCAD 用户配置.$\r$\n\
						这也会删除所有已安装的 FreeCAD 插件，并会影响所有FreeCAD的偏好配置.$\r$\n\
						你确定要继续吗?'
${LangFileString} SecUnProgramFilesDescription "卸载 FreeCAD 及其所有组件."
