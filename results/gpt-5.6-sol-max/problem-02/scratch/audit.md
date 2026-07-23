# Final proof audit notes

- Ray orders: At B, `K inside angle LBA` means BK lies between BL and BA. Since L is inside BNC, L is inside triangle BNC and hence BL is inside angle ABC; K inside BMC similarly BK inside ABC. So BA-BK-BL-BC valid because given y=LBK and interiors. At C, `L inside angle ACK` means CL lies between CA and CK; both inside ACB, giving CA-CL-CK-CB.
- Angles BCK = gamma-x-z due CA->CL x, CL->CK z, rest gamma-x-z. KBC = beta-x (BA->BK x). BKC = pi-(beta-x)-(gamma-x-z)=alpha+2x+z.
- LBC = beta-(x+y), BCL=gamma-x, BLC=alpha+2x+y.
- Trig generic equation checked from equating lengths and sine rule.
- Identity (11) numerically and symbolically valid; `derive_E_check.py` did not simplify its difference automatically but numerical/manual expansion confirms: divide desired identity by U; expansion gives H. Need perhaps include a derivation if concern.
- F relation signs match numeric tests and scripts.
- Coordinates CL direction = angle alpha+pi+x, vector (-cos(alpha+x),-sin(alpha+x)); valid ray order at C.
- Circumcentre existence convention implies AKL noncollinear. If one worries statement could name circumcentre only when nondegenerate, accepted.
- V positive: alpha+x < pi? Since x < gamma? At C CL makes x from CA and is interior angle ACB, so x<gamma; alpha+x<alpha+gamma=pi-beta<pi. yes.
- U positive: x>0 because K strictly inside angle LBA, so ray not BA; x<pi. All divisions safe. t=y,z positive by strict ray/point interiors and defining angle equalities; sin theta positive.
- Scaling normalization valid under similarity.
- Sparse certificate exact verified.
- Null character accidentally inserted in Approaches current.md line; should sanitize before final.
