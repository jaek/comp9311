# SQL Operations

| Catalogue   |                  |             |          |
| ----------- | ---------------- | ----------- | -------- |
| item_name   | manufacture_date | description | quantity |
| "hat"       | 11/12/1998       | "hat"       | 1235     |
| "shoe"      | 1/4/1995         | "foot hat"  | 123      |
| "underpant" | 4/7/1969         | "willy hat" | 12       |

## SELECT

"Selects" a subset of the specified relation(s), based on given criteria.
For example, the following query would yield:

    SELECT item_name, manufacture_date
    FROM catalogue
    WHERE quantity > 100;

| Selection |            |            |      |
| --------- | ---------- | ---------- | ---- |
| "hat"     | 11/12/1998 | "hat"      | 1235 |
| "shoe"    | 1/4/1995   | "foot hat" | 123  |
