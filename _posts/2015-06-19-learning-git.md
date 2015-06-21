---
layout: post
title: Git tips
---
Tips for myself for git

![Git transport model]({{ site.url }}/assets/git-transport.png)

## git add

- `git add -N <file>` adds a file, but does not stage the changes in the file to the index. This allows you to split the changes to this file into atomic commits

- `git add -A` adds and removed all added and deleted files from the index and stages all changes. It is not equivalent to `hg addremove` because it stages all changes to the index

## git commit

- `git commit -a` stages all changes to tracked files and removes any deleted files from the index. This is equivalent to `git add -u; git commit`

- `git commit --amend` appends the current staged edits to the previous commit, creating a new commit. Add `--no-edit` to keep the same commit message

## git checkout

- `git checkout <rev> -- <file>`, leave `<rev>` empty if you want to update to the current index, or use `HEAD` to update to the local repository

## git diff

{% highlight diff %}
diff --git a/importantFile b/importantFile
new file mode 100644
index 0000000..3d44acd
--- /dev/null
+++ b/importantFile
@@ -0,0 +1,2 @@
+important stuff
+crazy change
{% endhighlight %}

- Notice the `0000000..3d44acd` is not the commit hash, but the file hash

## git log

- `git log --graph --decorate --oneline $(git rev-list -g --all)` shows all the branches, including unnamed ones and stashes

- `git log -p` shows detailed commits

## git push

- `git push --all origin` pushes a new branch (don't necessarily need origin - only if you have multiple upstreams)

- `git push --set-upstream origin thirdbranch` pushes the current branch and sets the remote as the upstream remote repository

- `git push origin master` will push the `master` branch to `origin` even if you are in a detached `HEAD` state

## git rebase

The standard workflow is as follows - we start with `HEAD` on the `master` branch tip. Then:

{% highlight bash %}
git checkout -b feature master # create a branch at the same point as the master branch
# add feature
git commit -am "Started developing a new feature"
# go back to master to make an important change - do this in another branch
git checkout -b quickfix master
# fix critical bug
git commit -am "Fixed bug"
git checkout master
git merge quickfix
git branch -d quickfix
{% endhighlight %}

Now, we have a fork. We could do a straight merge of the feature, or we could use a rebase - this retains linear history. It must be certain that no one else has pulled the feature branch, as this will be removed and re-written by a set of entirely different commits

{% highlight bash %}
git checkout feature
git rebase master
{% endhighlight %}

At this point, the history looks like

{% highlight %}
* cc2bfa3 (HEAD, feature) Started developing a new feature
* b000ff1 (master) Fixed bug
{% endhighlight %}

Now, we have to do a fast forward merge (this is an easy merge, it's just moving the branch head location forward a few commits)
{% highlight %}
git checkout master
git merge feature
git branch -d feature
{% endhighlight %}

And we have fully integrated
## git reset

- `git reset` unstages all files, allowing you to recreate the commit snapshot from scratch, but it leaves the working directory unchanged. Adding `--hard` destroys all changes in the working directory, so there are no differences to be unstaged. It resets the working directory to the original commit
