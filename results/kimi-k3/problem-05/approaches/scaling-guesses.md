# Approach: quick guesses by scaling

## Status
Dead end for classification, but useful for finding the candidate family.

## What was tried
- Constant functions $f\equiv c$ fail: the right inequality would give $c+y\ge2\sqrt{cx}$ for all $x,y>0$, impossible by fixing $y$ and taking $x$ large.
- Power functions $f(x)=x^a$ fail except for $a=1$. One quick test is $y=x^a$: then $f(x)=x^a$ and $f(y)=x^{a^2}$, so the right inequality becomes
  \[
  x^a\ge x^{(1+a^2)/2}\qquad(x>0).
  \]
  If $a\ne1$, then $a-(1+a^2)/2=-(a-1)^2/2<0$, and the inequality fails as $x\to\infty$.
- The identity $f(x)=x$ works. More importantly, the translation $f(x)=x+c$ also works, because then
  \[
  f(x)+y=x+c+y=x+f(y),
  \]
  so the middle expression is the arithmetic mean of the same two numbers $x$ and $f(y)=y+c$ appearing in the outer means.

## Lesson
The correct candidate family is larger than just the identity: it is all translations by a nonnegative constant. The rest of the work is to prove that the increment $f(x)-x$ cannot vary with $x$.
