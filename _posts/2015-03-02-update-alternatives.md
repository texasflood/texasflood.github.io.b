---
layout: post
title: Update alternatives
---

Say you messed up your alternatives for liblapack.so.3, but you had the output from the --display option:

{% highlight bash %}
liblapack.so.3 - auto mode
  link currently points to /usr/lib/lapack/liblapack.so.3
/usr/lib/atlas-base/atlas/liblapack.so.3 - priority 5
  slave liblapack.so.3gf: /usr/lib/atlas-base/atlas/liblapack.so.3
/usr/lib/lapack/liblapack.so.3 - priority 10
  slave liblapack.so.3gf: /usr/lib/lapack/liblapack.so.3
Current 'best' version is '/usr/lib/lapack/liblapack.so.3'.
{% endhighlight %}

Then run these commands to restore your alternatives:

{% highlight bash %}
sudo update-alternatives --remove-all liblapack.so.3

sudo update-alternatives --install /usr/lib/liblapack.so.3 liblapack.so.3 /usr/lib/lapack/liblapack.so.3 10 --slave /usr/lib/liblapack.so.3gf liblapack.so.3gf /usr/lib/lapack/liblapack.so.3

sudo update-alternatives --install /usr/lib/liblapack.so.3 liblapack.so.3 /usr/lib/atlas-base/atlas/liblapack.so.3 5 --slave /usr/lib/liblapack.so.3gf liblapack.so.3gf /usr/lib/atlas-base/atlas/liblapack.so.3

sudo update-alternatives --auto liblapack.so.3
{% endhighlight %}

Bonus points to anyone who can write a script to automate this.
