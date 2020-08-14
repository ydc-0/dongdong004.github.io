# VS code

## 下载安装
- windows/linux 均可以直接下载安装

## 推荐插件

### 常用
- vscode-icons
- Markdown All in One
- GitLens (must put git in PATH)
- Code Runner
- Python
- C/C++

### 推荐
- Prettier - Code formatter
- Test Explorer UI
  - Python Test Explorer for Visual Studio Code
- PlantUML

## 实用命令
- 快速输入命令：CTRL+SHIFT+P
  - Python: Select Linter (set formatter for python)
- 块选中, 多行: SHIFT+ALT+MOUSE
  - 起始点为当前光标所在位置
  - 编辑多行的时候很有用
- 快速选中当前 word， 选中下一个相同的项： CTRL+D
  - 立刻选中所有： CTRL+SHIFT+L
  - 可用于重命名
  - F2 重命名依赖于：python-rope 等


### 填坑
- TAB 键变为菜单跳转 (Tab Moves Focus) -> CTRL+M 解决

## Settings
- settings.json
  ```
  {
      "files.autoSave": "onFocusChange",
      "editor.formatOnSave": false,
      "workbench.iconTheme": "vscode-icons",
      // python formatting
      "python.linting.flake8Args": [
          "--max-line-length=120",
      ],
      "python.formatting.autopep8Args": [
          "--max-line-length=120",
      ],
      "python.linting.pylintEnabled": false,
      "python.linting.flake8Enabled": true,
      "python.linting.enabled": true,
      //python unit test: pytest
      "python.testing.unittestEnabled": false,
      "python.testing.nosetestsEnabled": false,
      "python.testing.pytestEnabled": true,
      // plantuml
      "plantuml.server": "http://www.plantuml.com/plantuml"
  }
  ```
