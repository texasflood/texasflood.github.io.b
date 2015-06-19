---
layout: post
title: Git tips
---
Tips for myself for git

![Git transport model]({{ site.url }}/assets/git-transport.png)

- `git checkout <rev> -- <file>`, leave `<rev>` empty if you want to update to the current index, or use `HEAD` to update to the local repository

- `git add -N <file>` adds a file, but does not stage the changes in the file to the index. This allows you to split the changes to this file into atomic commits

- `git commit -a` stages all changes to tracked files and removes any deleted files from the index. This is equivalent to `git add -u; git commit`

- `git add -A` adds and removed all added and deleted files from the index and stages all changes. It is not equivalent to `hg addremove` because it stages all changes to the index
