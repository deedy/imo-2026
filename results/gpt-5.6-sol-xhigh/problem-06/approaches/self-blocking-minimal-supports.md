# Self-blocking minimal prime supports

## Idea
Replace every integer by its set of prime divisors. Let $\mathcal G$ be the supports of the sequence terms and let $\mathcal F$ consist of all finite prime sets meeting every member of $\mathcal G$. The recurrence, together with the freedom to take a large integer with any prescribed finite prime support, proves $\mathcal G=\mathcal F$. Thus $\mathcal F$ is upward-closed, intersecting, and self-blocking.

The inclusion-minimal members $\mathcal H$ determine the entire family. The main task is proving that their union is finite.

## Status
Successful.

## Details
For $p\in H\in\mathcal H$, define
\[
c(H,p)=\prod_{q\in H\setminus\{p\}}q.
\]
If $c(H,p)>a_1$, the integer $c(H,p)$ is not selected because its support is the proper subset $H\setminus\{p\}$ of the minimal member $H$. Therefore an earlier selected integer is coprime to it. A minimal support $K$ inside that earlier term must meet $H$, and it cannot meet $H\setminus\{p\}$, so it contains $p$. Moreover $c(K,p)<c(H,p)$. Descent produces $H$ with $c(H,p)\le a_1$.

There are finitely many possible cores $C=H\setminus\{p\}$ of product at most $a_1$. For a fixed core $C$, minimality gives $C\notin\mathcal F$, so self-blocking supplies a finite member $F_C\in\mathcal F$ disjoint from $C$. If $C\cup\{p\}\in\mathcal H$, intersection forces $p\in F_C$. Thus each core permits finitely many $p$, and the union of $\mathcal H$ is finite.

The selected integers are then exactly those divisible by the squarefree product associated with at least one $H\in\mathcal H$. This predicate is periodic modulo the product of all relevant primes.