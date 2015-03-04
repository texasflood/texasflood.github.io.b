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

sudo update-alternatives --install /usr/lib/liblapack.so.3 liblapack.so.3 /usr/lib/lapack/liblapack.so.3 10 \
--slave /usr/lib/liblapack.so.3gf liblapack.so.3gf /usr/lib/lapack/liblapack.so.3

sudo update-alternatives --install /usr/lib/liblapack.so.3 liblapack.so.3 /usr/lib/atlas-base/atlas/liblapack.so.3 5 \
--slave /usr/lib/liblapack.so.3gf liblapack.so.3gf /usr/lib/atlas-base/atlas/liblapack.so.3

sudo update-alternatives --auto liblapack.so.3
{% endhighlight %}

Or the more complex example:
{% highlight bash %}
libblas.so.3 - auto mode
  link currently points to /usr/lib/atlas-base/atlas/libblas.so.3
/usr/lib/atlas-base/atlas/libblas.so.3 - priority 35
  slave libatlas.so.3: /usr/lib/atlas-base/libatlas.so.3
  slave libatlas.so.3gf: /usr/lib/atlas-base/libatlas.so.3
  slave libblas.so.3gf: /usr/lib/atlas-base/atlas/libblas.so.3
  slave libcblas.so.3: /usr/lib/atlas-base/libcblas.so.3
  slave libcblas.so.3gf: /usr/lib/atlas-base/libcblas.so.3
  slave libf77blas.so.3: /usr/lib/atlas-base/libf77blas.so.3
  slave libf77blas.so.3gf: /usr/lib/atlas-base/libf77blas.so.3
  slave liblapack_atlas.so.3: /usr/lib/atlas-base/liblapack_atlas.so.3
  slave liblapack_atlas.so.3gf: /usr/lib/atlas-base/liblapack_atlas.so.3
/usr/lib/libblas/libblas.so.3 - priority 10
  slave libblas.so.3gf: /usr/lib/libblas/libblas.so.3
Current 'best' version is '/usr/lib/atlas-base/atlas/libblas.so.3'.
{% endhighlight %}

Then run:

{% highlight bash %}
sudo update-alternatives --install /usr/lib/libblas.so.3 libblas.so.3 /usr/lib/atlas-base/atlas/libblas.so.3 35 \
--slave /usr/lib/libatlas.so.3 libatlas.so.3 /usr/lib/atlas-base/libatlas.so.3 \
--slave /usr/lib/libatlas.so.3gf libatlas.so.3gf /usr/lib/atlas-base/libatlas.so.3 \
--slave /usr/lib/libblas.so.3gf libblas.so.3gf /usr/lib/atlas-base/atlas/libblas.so.3 \
--slave /usr/lib/libcblas.so.3 libcblas.so.3 /usr/lib/atlas-base/libcblas.so.3 \
--slave /usr/lib/libcblas.so.3gf libcblas.so.3gf /usr/lib/atlas-base/libcblas.so.3 \
--slave /usr/lib/libf77blas.so.3 libf77blas.so.3 /usr/lib/atlas-base/libf77blas.so.3 \
--slave /usr/lib/libf77blas.so.3gf libf77blas.so.3gf /usr/lib/atlas-base/libf77blas.so.3 \
--slave /usr/lib/liblapack_atlas.so.3 liblapack_atlas.so.3 /usr/lib/atlas-base/liblapack_atlas.so.3 \
--slave /usr/lib/liblapack_atlas.so.3gf liblapack_atlas.so.3gf /usr/lib/atlas-base/liblapack_atlas.so.3 

sudo update-alternatives --install /usr/lib/libblas.so.3 libblas.so.3 /usr/lib/libblas/libblas.so.3 10 \
--slave /usr/lib/libblas.so.3gf libblas.so.3gf /usr/lib/libblas/libblas.so.3
{% endhighlight %}

<p>
Explanation: the first argument to {% ihighlight bash %}update-alternatives --install{% endihighlight %}is the generic link which programs will actually use to link shared objects or execute a binary such as {% ihighlight bash %}editor{% endihighlight %}. The second argument is just the name of the program, which is usually just chosen to be the actual filename of the generic link. This is the name that will appear in the {% ihighlight bash %}/etc/alternatives{% endihighlight %} directory. The third argument is the path of the actual location of the binary/shared object/whatever else file. The fourth is the priority - the higher, the more preferential.
</p>

<p>
Then we have the slaves which take only three arguments - these correspond to the three arguments for the master link. Basically, these don't actually have to have <em>anything</em> to do with the master link, but in practice, they would be related, e.g. by all the slaves being versions of a program. E.g. if you had Vim v6 and v7, you could have a master for v6 and v7, and the slaves of these would be ex, vimdiff, view etc. Then say you wanted to upgrade to v7, you just run one command and all v6 copies of ex, vimdiff and view get updated to v7!
</p>

<p>
But in general, they exist as links just like the master link, and can link to totally different, or the same object. In the above example for libblas.so.3, if we are using /usr/lib/atlas-base/atlas/libblas.so.3, then /usr/lib/libatlas.so.3gf exists. But if we change the configuration via --set to point to /usr/lib/libblas/libblas.so.3, then /usr/lib/libatlas.so.3gf is removed.
</p>

<p>
Bonus points to anyone who can (be bothered to) write a script to automate this.
</p>
