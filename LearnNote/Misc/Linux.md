
## 实用技巧
### 修改系统默认的 python 版本
- 用户级修改
  - 将 `alias python='python3'` 添加到 .bashrc
- 修改软链接
  - `sudo rm /usr/bin/python`
  - `sudo ln -s /usr/bin/python3.5 /usr/bin/python`
- 基于update-alternatives
  - `sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1`
  - `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2`
  - 最后一个参数为优先级，优先级高则默认
  - 列出支持的 python 版本 `update-alternatives --list python`
  - 替换 python 版本 `update-alternatives --config python`
- 使用 pyenv
  - https://github.com/pyenv/pyenv

## 为特定软件设置权限
- 例： 为 python 设置抓包权限
- https://medium.com/@badbot/safe-packet-capture-python-without-sudo-b08c4c4e531
- `sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' .venv/bin/python3`
- `getcap .venv/bin/python3`