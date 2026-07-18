# Iteration and rigidity

**Idea.** Put \(x=f(y)\). Both outer terms then equal \(f(y)\), forcing
\[
f(f(y))=2f(y)-y.
\]
Writing \(g(t)=f(t)-t\), this says \(g(f(t))=g(t)\), so the forward iterates are \(f^n(t)=t+ng(t)\). Positivity gives \(g\ge 0\).

Next compare two points by putting \(x=f(u),y=v\), and then swapping \(u,v\). This yields the key quadratic estimate
\[
|g(u)-g(v)|\le (\sqrt{f(u)}-\sqrt{f(v)})^2.
\]
It implies that \(f\) is strictly increasing. Increasingness of every iterate, followed by \(n\to\infty\), implies that \(g\) is nondecreasing. The quadratic estimate rules out either one-sided jump of this monotone function, so \(g\) is continuous. Finally, partitioning an interval and summing the quadratic estimate makes its total variation vanish. Thus \(g\) is constant and \(f(x)=x+c\), \(c\ge0\).

**Status:** successful; this gives the complete characterization.
