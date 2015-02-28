---
layout: post
title: Proof that the complementary CDF equals the expected value for non-negative RVs
---
This is a cool result which I've sketched out a (possibly overly detailed) way to prove.

<strong><em>
Definitions:
</em></strong>

<p align="center">
<div class="Math">
$$F_X(x)=P(X\leq x)$$
$$f_x(x)=\frac{dF_X(x)}{x}$$
$$s_X(x)=\int_x^\infty f_X(t)dt$$
<p align="center">
$X$ is <em>almost surely</em> non-negative and continuous
</p>
</div>
</p>

<strong><em>
Theorem:
</em></strong>

If $X \in \mathbb{R^+_0} $ is a random variable, then:

<div class="Math">
$$\int_0^\infty (1-F_X (x))dx = E[X] $$
</div>

It seems a bit surprising at first, but then it seems obvious - until you try to prove it, then it's confusing!

<strong><em>
Proof:
</em></strong>

<div class="Math">
Let's start from the definition of $E[X]$:

$$E[X] = \int_{-\infty}^{\infty}xf_X(x)dx = \int_{0}^{\infty}xf_X(x)dx$$
</div>

<div class="Math">
As $f_X(x)=0\; \forall\; x < 0$.
</div>
<BR>

The obvious thing to do here is integrate by parts:

<div class="Math">
$$\int u\frac{dv}{dx}dx = uv - \int v\frac{du}{dx}dx$$

<p>
What do we choose to be $u$ and $dv/dx$? As always, we choose whatever simplifies the integral - differentiating $x$ gives a simpler result than integrating $x$. Integrating $f_X(x)$ gives $F_X(x)$ which is actually part of the result, so this seems like the way to go!
</p>

<p>
Set $u=x$ and $v'=f_X(x)$. Now we need the integral of $f_X(x)$, but integration is only defined up to a constant, so let's take $v(x)=F_X(x)-1$. If you're new to calculus, this might not seem allowed - surely this will change the result? The answer is it won't - it will just change the appearance. Look again at the left hand side of the formula for integration by parts and say we added a constant $C$ to $v$:

$$u(v+C) - \int (v+C)\frac{du}{dx}dx$$
$$=uv - \int v\frac{du}{dx}dx + uC - C\int \frac{du}{dx}dx$$
$$=uv - \int v\frac{du}{dx}dx + uC - uC $$
$$=  uv - \int v\frac{du}{dx}dx$$

By the definition of integration.
</p>

<p>
Now we have:
$$E[X] = [x(F_X(x)-1)]_0^\infty + \int_0^\infty(1-F_X(x))dx$$

We're nearly there, we just need to prove $[x(F_X(x)-1)]_0^\infty = 0$. A classic method to prove something equals 0 is to prove it must be $\geq 0$ and it also must be $\leq 0$.
</p>

<p>
Now as $F_X(x)=P(X\leq x)$ then $1 - F_X(x) = P(X>x)=\int_x^\infty f_X(t)dt$. Define $s_X(x)=\int_x^\infty f_X(t)dt$ for convenience.
</p>

<p>
Back to that pesky $uv$ term:

$$-[xs_X(x)]_0^\infty = xs_X(x)|_{x=0} - xs_X(x)|_{x\rightarrow\infty}$$
$$= - xs_X(x)|_{x\rightarrow\infty}$$

As $xs_X(x)|_{x=0} = 0$. Now $x\geq 0$ and $s_X(x)\geq 0$ as $f_X(x)\geq 0$, all by or obvious from definition.
$$\therefore -xs_X(x)|_{x\rightarrow\infty} \leq 0$$
</p>

<p>
Now comes the cool bit - pay attention:
$$-xs_X(x)|_{x\rightarrow\infty} = -\lim_{x\to \infty}x\int_x^\infty f_X(t)dt$$
$$\geq -\lim_{x\to \infty}\int_x^\infty t f_X(t)dt$$
The last step just needs you to realise that when you move $x$ to inside the integral and change it to $t$, it is always larger than $x$ itself since the integral is going from $x$ to $\infty$, so the smallest value of $t$ is $x$ and the largest is $\infty$ at the limit of the integral.
</p>

<p>
Now the finishing touch:
$$-\lim_{x\to \infty}\int_x^\infty t f_X(t)dt = 0$$
Why? Because as you take the limit of the integral as $x \to \infty$, you are squeezing the range of the integral to nothing, it becomes:
$$-\int_\infty^\infty t f_X(t)dt$$

so
$$0 \leq -xs_X(x)|_{x\rightarrow\infty} \leq 0$$
$$\therefore -xs_X(x)|_{x\rightarrow\infty}=0$$ 
</p>

$$E[X] = -[xs_X(x)]_0^\infty + \int_0^\infty(1-F_X(x))dx$$
$$=\int_0^\infty(1-F_X(x))dx$$
</p>

$$\tag*{$\blacksquare$}$$

</div>

<em>If you see any errors or want clarification, post a comment.</em>
