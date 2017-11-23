# Git

## untract file if file have been in GitHub
- use .gitignore still tract the change in file
- use `git rm --cached` will remove file in GitHub
- use `git update-index --assume-unchanged `, it works!!!, just untrack file, and it don't have any side effect


## Undo
- undo `git add .`, use `git reset`