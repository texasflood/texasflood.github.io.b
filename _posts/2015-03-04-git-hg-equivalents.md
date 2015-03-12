---
layout: post
title: Git and Mercurial equivalents
---

This is a list I will add to as time goes by:

<table>
  <col>
  <col>
  <col width="330">
  <thead>
    </tr>
      <th>Git</th>
      <th>Mercurial</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <centering>
    <tr>
      <td><code>git clean -fd</code></td>
      <td><code>hg purge</code></td>
      <td>Deletes all newly added untracked file and directories</td>
    </tr>
    <tr>
      <td><code>git add .</code><br>
          <code>git ls-files --deleted | xargs git rm</code></td>
      <td><code>hg addremove</code></td>
      <td>Adds all untracked files and removes all missing files</td>
    </tr>
    </centering>
  </tbody>
</table>
