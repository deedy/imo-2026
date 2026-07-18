# Scratch notes

- Initial mistake to avoid: only noticing $f(x)=x$. In fact $f(x)=x+c$ works for every $c\ge0$.
- Core identity: with $v=f(y)$,
  $4xv=(x+v)^2-(x-v)^2$ and $2(x^2+v^2)=(x+v)^2+(x-v)^2$.
- Substituting $x=f(y)$ is the equality-forcing move. It gives $f(f(y))=2f(y)-y$ directly from the combined estimate.
- If $p=f-\mathrm{id}$ took values $c>d$, the left inequality creates a forbidden interval for a $c$-increment point. Enlarge the $d$-point by iterating it forward so the interval is wider than the spacing $c$ of the other orbit.
