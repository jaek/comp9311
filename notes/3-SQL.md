# SQL Operations

**(1)** The ````Catalogue```` relation:

| Catalogue   |                  |             |          |
| ----------- | ---------------- | ----------- | -------- |
| item_name   | manufacture_date | description | quantity |
| "hat"       | 11/12/1998       | "hat"       | 1235     |
| "shoe"      | 1/4/1995         | "foot hat"  | 123      |
| "underpant" | 4/7/1969         | "willy hat" | 12       |

## Queries
---

### SELECT - Projection

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

### WHERE - Selection

The operation ````WHERE```` denotes (selects) a subset of a relation.
In relational algebra, the selection operation uses the Greek letter *sigma* - σ.

### AS - rename

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

## Subqueries
---

### IN - check if tuple is in relation

The ````IN```` function takes a set of tuples *T*
and returns ````TRUE```` if *T* is contained in *R*.

Given the tuple ````Item_weights```` (2):

| Item_weights| ------ |
| ----------- | ------ |
| name        | weight |
| "underpant" | 10.0   |
| "leg"       | 1.2    |

    SELECT *
    FROM catalogue c,
    WHERE c.item_name
        IN (SELECT name
            FROM Item_weights);

Would yield the tuple:

| item_name   | manufacture_date | description | quantity |
| ----------- | ---------------- | ----------- | -------- |
| "underpant" | 4/7/1969         | "willy hat" | 12       |

### EXISTS - check if relation is non-empty

For example, to find out if there are any items in ````Item_weights```` with the same name as an item in ````Catalogue````:

    SELECT *
    FROM catalogue c
    WHERE EXISTS
        (SELECT name
         FROM Item_weights w
         WHERE w.name = c.item_name
          );

Which would yield the tuples:

| item_name   | manufacture_date | description | quantity |
| ----------- | ---------------- | ----------- | -------- |
| "underpant" | 4/7/1969         | "willy hat" | 12       |

Or conversely, to find all items in our catalogue which do not have corresponding tuples in ````Item_weights````:


    SELECT *
    FROM catalogue c
    WHERE NOT EXISTS
        (SELECT name
         FROM Item_weights w
         WHERE w.name = c.item_name
          );


| Catalogue   |                  |             |          |
| ----------- | ---------------- | ----------- | -------- |
| item_name   | manufacture_date | description | quantity |
| "hat"       | 11/12/1998       | "hat"       | 1235     |
| "shoe"      | 1/4/1995         | "foot hat"  | 123      |

## Set Operations
---

Set operations in SQL take a number of query results and combine them into a single result set.

### Union

The ````UNION```` operation combines the output of two queries *Q1* and *Q2*
into a single result table consisting of all matching tuples.
Consider the relation ````new_stock```` (3)

| new_stock |                  |
| --------- | ---------------- |
| item_name | manufacture_date |
| "hat"     | 11/12/2007       |
| "shoe"    | 1/4/1995         |

    SELECT c.item_name, c.manufacture_date
    FROM Catalogue c
    UNION
    SELECT *
    FROM new_stock;

| item_name | manufacture_date |
| --------- | ---------------- |
| "hat"     | 11/12/2007       |
| "hat"     | 11/12/1998       |
| "shoe"    | 1/4/1995         |

### Intersection

The SQL INTERSECT operator takes the results of two queries and returns only rows that appear in both result sets.

The following example INTERSECT query returns all rows from the Orders table where Quantity is between 50 and 100:

    SELECT *
    FROM   Orders
    WHERE  Quantity BETWEEN 1 AND 100
    INTERSECT
    SELECT *
    FROM   Orders
    WHERE  Quantity BETWEEN 50 AND 200;

### Difference

---

## Aggregation

Aggregation operators in SQL apply to a list of numeric values in one column:

| operator | description                        |
| -------- | ---------------------------------- |
| SUM      | The sum total of all values in *X* |
| AVG      | The average of all values in *X*   |
| MIN      | The smallest value in *X*          |
| MAX      | The largest value in *X*           |
| COUNT    | The number of values in *X*        |

---
# SQL data types

Refer to [this SQL file](/scripts/notes.sql) for more info.

SQL data types represent the most fundamental form of constraint/domain checking.
The type system ensures that data can only be stored in certain formats.

* Numbers: integers and real numbers
* Characters: Strings and characters of different lengths
* Dates and times

In addition, it is possible to specify more complex types.  

These types can be used to enforce more complex domain membership conditions, i.e
we can ensure that a given column never contains a negative number, or that a piece of
text never contains the phrase ````')DROP TABLE students;````

From the PostgreSQL docs:
> Data types are a way to limit the kind of data that can be stored in a table. For many applications, however, the constraint they provide is too coarse. For example, a column containing a product price should probably only accept positive values. But there is no standard data type that accepts only positive numbers. Another issue is that you might want to constrain column data with respect to other columns or rows. For example, in a table containing product information, there should be only one row for each product number.


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
| division          |              | ÷             |            |
| cartesian product | CROSS JOIN   | X             |            |
| natural join      | NATURAL JOIN | ⋈             |            |
| inner join        | INNER JOIN   | ⋈<sub>θ</sub> | *wθx, wθv* |
| equi-join         |              |               | *w=x, w=v* |
| left outer join   |              |               |            |
