**Let *F = {A->B, AB->D, CE->G, C->H}***

**Does *F|= AC->G*?**

>  A+ = A, B, D
>
>  C+ = C, H
>
>  :. AC+ = A, B, C, D, H
>
>  G ∉ AC+
>
>  :. F |≠ AC->G

**Let *F = {A->C, BC->D}* and *R = (A,B,C,D)***
**Find the highest normal form:**

1) Each attribure of *R* is atomic, therefore it is in 1NF
2) The primary key for R is (A,B). A->C, therefore this table does not satisfy 2NF with respect to F

**let *F = {Y->X, Z->XYW}***

>let F' = {
  Y->X
  Z->X
  Z->Y
  Z->W
}

We cannot remove Y->X:
>
>F'(-Y->X)+ = {XZW}

We can remove Z->X:
>
>F'(-Z->X)+ = {YXZW}

We cannot remove Z->Y or Z->W:
>
F'(-Z->Y)+ = {XZW}
F'(-Z->W)+ = {XYZ}

>minimum cover is {Y->X, Z->W, Z->Y}
