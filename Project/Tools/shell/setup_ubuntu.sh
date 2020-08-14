set -e

# sudo apt-get purge libappstream3
sudo apt-get update
sudo apt-get install tree make vim

# git
sudo apt-get install git gitk
# git config --global user.name "Aiden"
# git config --global user.email "aiden@example.com"
git config --global core.editor vim
git config --global credential.helper store
git config --global --replace-all core.pager "less -F -X"

# pyenv
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv/pyenv-1.2.19"' >> $HOME/.pyenv/active
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> $HOME/.pyenv/active
echo 'if command -v pyenv 1>/dev/null 2>&1; then' >> $HOME/.pyenv/active
echo '    eval "$(pyenv init -)"' >> $HOME/.pyenv/active
echo 'fi' >> $HOME/.pyenv/active
echo 'source $HOME/.pyenv/activate' >> $HOME/.profile

# python
sudo apt-get install --no-install-recommends \
    make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
source $HOME/.pyenv/activate
pyenv install python3.7.7
pyenv global 3.7.7
python -m pip install --upgrade pip
pip install pytest flake8 pep8-naming cython pyyaml dpkt Jinja2 numpy matplotlib\
    pyserial netifaces xunitgen xunitparser \
    pygame rope

# zsh
sudo apt-get install zsh curl wget
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
echo "source $HOME/.profile" >> $HOME/.zshrc

# for vs-code plantuml 
# "plantuml.server": "http://www.plantuml.com/plantuml"
sudo apt-get install openjdk-11-jdk graphviz