---
layout: post
title: Send emails from your gmail account from the command line
---
This provides a passwordless solution for Debian based distros by using gnome-keyring


{% highlight bash %}

sudo apt-get install gnome-keyring msmtp msmtp-gnome
vim ~/.msmtprc

{% endhighlight %}

And add the following:

{% highlight bash %}
#Gmail account
defaults
account gmail
auth on
host smtp.gmail.com
from userAddress@gmail.com
auth on
tls on
tls_trust_file /usr/share/ca-certificates/mozilla/Equifax_Secure_CA.crt
user userAddress@gmail.com
port 587

account default : gmail
{% endhighlight %}

Now use the tool to set your password:

{% highlight bash %}
wget -P ~/Downloads http://texasflood.github.io/assets/msmtp-gnome-tool.py
#wget -P ~/Downloads https://raw.githubusercontent.com/tom111/mail-setup/master/msmtp-gnome-tool.py # if you want the latest original version
chmod u+x ~/Downloads/msmtp-gnome-tool.py
~/Downloads/msmtp-gnome-tool.py -s -u userAddress@gmail.com -e smtp.gmail.com
{% endhighlight %}

This way, your password is not stored in plaintext and you can still send emails without being prompted for your password.

And now you should be able to send emails like so:

{% highlight bash %}
echo -e "Subject: Hello\r\n""$(cat fileName)" | msmtp recipient@hotmail.com
echo -e "Subject: A different subject\nMessage contents" | msmtp recipient@hotmail.com
echo -e "Message contents" | msmtp recipient@hotmail.com
{% endhighlight %}
 
