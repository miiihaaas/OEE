# OEE
Overall Efficiency of Equipment

## izgled aplikacije
1 = ekstrudiranje
    11 = ZSK43
        110 = ekstrudiranje
        111 = čišćenje
        112 = čišćenje radnog mesta
        113 = čekanje probe sa mlina
        114 = kontrola
        115 = kvar
        116 = nema premiksa
        117 = nema konejnera za čips
        118 = zagrevanje
        119 = nema operatera
    12 = APV
        120 = ekstrudiranje
        121 = čišćenje
        122 = čišćenje radnog mesta
        123 = čekanje probe sa mlina
        124 = kontrola
        125 = kvar
        126 = nema premiksa
        127 = nema konejnera za čips
        128 = zagrevanje
        129 = nema operatera
2 = mlevenje
    21 = ACM20
      210 = mlevenje
      211 = čišćenje
      212 = čišćenje radnog mesta
      213 = kontrola
      214 = kvar
      215 = nema čipsa
      216 = pražnjenje filtera
      217 = nema operatera
    22 = ACM30
      220 = mlevenje
      221 = čišćenje
      222 = čišćenje radnog mesta
      223 = kontrola
      224 = kvar
      225 = nema čipsa
      226 = pražnjenje filtera
      227 = nema operatera

## aktivirano dugme (npr: 112 = čišćenje radnog mesta) treba da vrati listu sa svim promenjivim
## u app fajlu treba da se dodeli ta lista new_record koja se dalje append u csv fajl

## input podataka se vrši preko QR koda (pokušaj u fajlu actions.py)
