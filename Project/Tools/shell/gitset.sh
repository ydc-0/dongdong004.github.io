git config --global user.name "Aiden"
git config --global user.email "aiden@example.com"
# set editor of git commit
git config --global core.editor vim
# store username and password when using https
git config --global credential.helper store
# Display the result directly if it's less than one screen
git config --global --replace-all core.pager "less -F -X"