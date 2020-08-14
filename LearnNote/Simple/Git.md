# 之前的部分
- [Git Doc](https://github.com/dongdong004/small_code/blob/master/document/git.md)
# 免密码
- SSH方式, 使用 ssh-key
- 创建文件存储
    ```bash
    touch ~/.git-credentials
    vim ~/.git-credentials
    https://{username}:{password}@github.com
    ```
- 凭证存储
  - [Caching your GitHub credentials in Git](https://docs.github.com/en/github/using-git/caching-your-github-credentials-in-gits)
  - [Git Tools - Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage)
  - 可选永久存储或一段时间内
    ```bash
    git config --global credential.helper cache
    git config --global credential.helper 'cache --timeout 3600'
    git config --global credential.helper store
    ```
- Https Url 免密
  - `git clone https://{username:password}@github.com/...`
  - `git remote set-url origin <url>`
# Zsh 清屏
- zsh 使用时，使用 git log/branch/diff 时必须使用 q 退出，且当前屏幕不保存之前的信息
- `git config --global --replace-all core.pager "less -F -X"`
  > passing the -F option to less causes it to quit if the content is less than one screen, 
  > however after doing so the screen is reset and you end up not seeing the content, 
  > the -X option does away with that behaviour. 

# git large file
- 
- https://ar.al/2019/10/19/install-git-lfs-on-a-raspberry-pi/