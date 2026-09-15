---
Subject: Useful git commits, branching, merging
Language: bash
Date: 2025-08-07
Time: 14:27
Tags:
  - "#snippet"
  - "#bash"
  - git
  - "#github"
---

# Status
```bash
git diff <file>  # The usual for unstaged
git status --staged <file> # Show staged commit diffs
```

# Commits 
Skipping the flake8/pre-commit bits
```bash
git commit -m "" --no-verify
```

# Log
``` bash
git log --graph --oneline --decorate --all  # Get complete graph log, simplified to one line
git log --graph --oneline --decorate  # Local branches only

# Set above up in config
git config --global alias.adog "log --all --decorate --oneline --graph"  # all branches
git config --global alias.dog "log --decorate --oneline --graph"  # local or interacted branches

# Then run for last 10 commits
git adog -n 10
```

# Branches
Fetch remote branches from origin
```bash
git fetch origin
git fetch --all
```

Check branches
```bash
git branch   # See local branches
git branch --all   # See local and remote branches
git branch -vv  # Extra verbose - see local branches, their attached remotes, and last commits
git branch -vva # Xtra verbose for awl
```

Checkout new branch, cloning from local
```bash
git checkout -b <new_branch>   # copies from current local
git checkout -b <new_branch> <cloned_branch>  # copies from specified local

git push --set-upstream origin <branch_name>  # First push to new branch
```

Checkout branch from remote which is not yet local
```bash
git checkout -b <local_branch_name> origin/<remote_branch_name>
```

Delete branch
```bash
git branch -d <branch_name>  # delete local branch only with merged commits
git branch -D <branch_name> # Force delete, including any uncommitted/merged changes
git push origin --delete <branch_name> # push delete request to origin 
```
# Merging
```bash
git checkout <branch>  # Switch to the target branch  
# OR
git merge <feature-branch>  # Merge changes from feature-branch into develop

# Then:
git push origin --delete <branch_name> # push delete request to origin 
```

# New Repo
## Create locally
1) Local init
```bash
git init -b main
git add .
git commit -m "Initial commit"
```
2) Create blank on github (no readme, license, gitignore), copy URL
3) Link and push to remote
```bash
git remote add origin <PASTE_YOUR_REMOTE_URL_HERE>
git push -u origin main
```

# Setup for LGeo Github
[LGeo Wiki](https://sites.google.com/lgeo.co/wiki/it-and-operations/github) - to be updated with info here

1) Make a new github account using your LGeo email
2) Ask for your GH account to be added to the LGeo Github organization (Himalya did for me)
4) Folks use either (or a combo) of command line and PyCharm integration for managing local repos