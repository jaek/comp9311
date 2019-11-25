# SQL Operations

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

For example, the following query:

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
