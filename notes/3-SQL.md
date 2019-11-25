# SQL Operations

**(1)** The ````Catalogue```` relation:

| Catalogue   |                  |             |          |
| ----------- | ---------------- | ----------- | -------- |
| item_name   | manufacture_date | description | quantity |
| "hat"       | 11/12/1998       | "hat"       | 1235     |
| "shoe"      | 1/4/1995         | "foot hat"  | 123      |
| "underpant" | 4/7/1969         | "willy hat" | 12       |

## SELECT - Projection

"SELECT" a subset of the specified relation(s), based on given criteria.

The ````SELECT```` operation is analogous to the relational algebra operation *projection*.
Represented by an upper case *pi* symbol - Π

For example, the following query on (1):

    SELECT item_name, manufacture_date -- attributes
    FROM catalogue                     -- relation(s)
    WHERE quantity > 100;              -- condition(s)

Yields

| item_name | manufacture_date |
| --------- | ---------------- |
| "hat"     | 11/12/1998       |
| "shoe"    | 1/4/1995         |


This query corresponds to:
Π<sub>{item_name, manufacture_date}</sub>(σ<sub>quantity > 100</sub>(Catalogue))

## WHERE - Selection

The operation ````WHERE```` denotes (selects) a subset of a relation.
In relational algebra, the selection operation uses the Greek letter *sigma* - σ.

## AS - rename

The operation ````AS```` takes an attribute *a* of relation *R*, and renames that attribute to *b*.

In relational algebra, the rename operation uses the Greek letter *rho* - ρ.

    SELECT item_name AS name
    FROM catalogue
    WHERE ((item_name IS NOT "NULL")
        AND
          description="willy hat");


expressed in relational algebra notation:

ρ<sub>(item_name/name)Π<sub>{item_name}</sub>(σ<sub>item_name != "NULL" AND description="willy hat"</sub> (Catalogue))

yields:

| Name        |
| ----------- |
| "underpant" |


## Cheat Sheet

### Unary Operators

Unary operators take one input (a relation *R*), and produce an output *R<sub>1</sub>.*

* Relation *R* with attributes (*a*<sub>1</sub>, *a*<sub>2</sub>, *a*<sub>3</sub>... *a*<sub>n</sub>)
* *A* ⊂ *R*
* *w, x ∊ *R*
* *y, z ∊ S*
* *B* is the set of binary operators { <, ≤, =, ≠, >, ≥ }
* *θ* ∊ *B*
* *v* is some constant value

| operation  | SQL    | algebra | predicate  |
| ---------- | ------ | ------- | ---------- |
| projection | SELECT | π / Π   | *A*        |
| selection  | WHERE  | σ       | *wθx, wθv* |
| rename     | AS     | ρ       | *wθv*      |


### Binary Operators

Unary operators take two inputs (relation *R*, *S*), and produce an output *R<sub>1</sub>.*

| operation         | SQL          | algebra       | predicate  |
| ----------------- | ------------ | ------------- | ---------- |
| cartesian product | CROSS JOIN   | X             |            |
| natural join      | NATURAL JOIN | ⋈             |            |
| inner join        | INNER JOIN   | ⋈<sub>θ</sub> | *wθx, wθv* |
| equi-join         |              |               | *w=x, w=v* |
