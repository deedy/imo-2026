# imo-2026-05 — tracking file

## Status
partial

## Problem
Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f :\mathbb{R}_{>0}\to \mathbb{R}_{>0}$ such that $\sqrt{\frac{x^2 + f(y)^2}{2}}\ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)}$ for every $x,y\in\mathbb{R}_{>0}$.

## Approaches tried
- Specialization and classical inequalities (RMS-AM-GM): when $x=f(y)$ both outer terms equal $x$, forcing $(f(x)+y)/2=x$ whenever $y\in f^{-1}(x)$. Outer comparison always true by $(x-f(y))^2\ge0$. When $x=y$ the ineq is automatic for any $f$.
- Tested $f(x)=cx$: right inequality always holds; left holds for all $x,y>0$ iff $c=1$. Verified algebraically (quadratic form discriminant $8(c^2-1)^2$) and numerically.
- Constants and $c/x$ fail (growth mismatch).
- Next: prove surjectivity of $f$ (or characterize image), then deduce $f(2x-f(x))=x$ on preimages, or prove $f(x)=x$ directly by other substitutions / taking infima.

## Current best
$f(x)=x$ works. It is the unique positive multiple of identity. Strong structural constraint: if $a\in\mathrm{im}(f)$ and $f(y)=a$ then necessarily $y=2a-f(a)$ (and this must be positive). Aim to prove $f=\mathrm{id}$ is the only solution.

## Full proof
(empty)
