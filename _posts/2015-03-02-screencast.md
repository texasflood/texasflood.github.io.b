---
layout: post
title: Screencasts in Ubuntu/Debian Sid
---

I've found that gtk-recordmydesktop, simplescreenrecorder and xvidcap. The bottom line is that they are all shit - the quality is poor, they take forever to encode the video once you're done with the recording etc. Especially gtk-recordmydesktop - it seems to do some extremely heavy compression on the videos under default settings which makes your videos look like a half downloaded corrupt avi you torrented. A lot of tweaking of parameters was attempted to no avail.

But then I found <a href="https://packages.debian.org/unstable/main/kazam">kazam</a> - and it works. It's fast, slick and most importantly, produces high quality videos.

{% highlight bash %}
sudo apt-get install kazam
{% endhighlight %}

Available on Ubuntu 12.04, 14.04 but only Debian Sid, unfortunately.
