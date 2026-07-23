exec(open('code/coeff_abstract.py').read().split("# S formula")[0])
# add d2 as expression abstract variable? N fixed. derive G coeff with t=d² symbol mentally use t placeholder replace D? create just list expressions text.
# G=L(l-kD)-l*t*(L-KE)
# coefficients:
# L*l=1-r(b+bi)+r²
# -L*kD= -kD + r bi kD
# -t l L + t l K E = -t[1-r(b+bi)+r²]+t[K E-r b K E]
# G0=(1-kD)-t(1-KE)
# G1=-(b+bi)+bi*kD + t*(b+bi)-t*b*K*E
# G2=1-t
print('G0 = 1-kD-t(1-KE)')
print('G1 = -(b+bi)+bi kD+t(b+bi)-t b KE')
print('G2 = 1-t')
