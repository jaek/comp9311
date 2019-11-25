# The Relational Model

The relational model is a model for database systems.
Information is described in terms of inter-connected relations.
Relational models are described using either mathematical or data oriented terms:

| mathematical | data-oriented | ER model    |
| ------------ | ------------- | ----------- |
| relation     | table         | entity type |
| tuple        | record        | entity      |
| attribute    | field/column  | attribute   |

*Note the similarity between ER and Relational Model concepts*

A relation or table can be represented as a  grid.
Each column represents an attribute/field
and each row represents a tuple/instance/record:

|         | Relation / Table A |           |           |
| ------- | ------------------ | --------- | --------- |
| Tuple 1 | attribute          | attribute | attribute |
| Tuple 2 | attribute          | attribute | attribute |
| Tuple 3 | attribute          | attribute | attribute |

Each attribute has an allowed range of values, referred to as its **domain**.

### mathematical description:

* A domain *D<sub>1</sub>* consists of **atomic** values of one type.
* For attribute *A* with domain *D*, *A<sub>1</sub>* ∈ *D<sub></sub>*
* A **relation schema** *R* is a set of attributes, i.e:

 *R(A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>...A<sub>n</sub>)*


### keys


As described in the [entity relationship model](/notes/1-entity-relationship_model.png),
a **superkey** of a relation is any set of attributes which can be used to uniquely identify a tuple.
For a given tuple, there may be several superkeys.


A **candidate key** *C* is a *minimal superkey*:
There is no superkey *S* of relation *R* which is a proper subset of *C*. There mayb be several candidate keys.

A **primary key** is a designated candidate key used throughout a DB to uniquely identify tuples of a given relation.

**Entity Integrity**: No attribute in a primary key can be NULL.

The **key constraint**:
In any tuple of a relation, there cannot be two relations having the same for their primary key attributes.

### Foreign Keys

Foreign keys refer to tuples in other relations.
In the relational model, a set of attributes *FK* from *R<sub>1</sub>*
may be a foreign key of *R<sub>2</sub>* with primary key *P* if
domain *D<sub>fk</sub>* of *FK* is the same as
domain *D<sub>p</sub>* of *P*:

| *R<sub>1</sub>*  |                  |     | *R<sub>2</sub>* |                 |
| ---------------- | ---------------- | --- | --------------- | --------------- |
| *FK*<sub>1</sub> | *FK*<sub>2</sub> | =   | *P*<sub>1</sub> | *P*<sub>2</sub> |









---

## Representing the relational model

Drawing a relational model representation of a database consists of a number of steps.
Taking the example of a simple database for an online shop:
The online shop must keep track of customers,
as well as the weight and contents of their orders.

### ER model step by step:

1. Identify entity types, and the attributes which describe them:

An initial model might look like this:

| Customer               | -             | -             |
| ---------------------- | ------------- | ------------- |
| <u>customer number</u> | {item number} | email address |

| Item               | -      |
| ------------------ | ------ |
| <u>item number</u> | weight |

Each entity type is uniquely identified with a primary key.

Note that:
- Each item entity can belong to many orders
- Each order can have many items
- Each customer can have many orders

**Relational databases do not support many-to-many relationships.**
Therefore, we must introduce some junction entities.
This entities will describe order details:

| Order               | -                      |
| ------------------- | ---------------------- |
| <u>order number</u> | <u>customer number</u> |

| Order_line          | -                  | -        |
| ------------------- | ------------------ | -------- |
| <u>order_number</u> | <u>item_number</u> | quantity |

And we can remove some attributes from the Customer entity:

| Customer               | -             |
| ---------------------- | ------------- |
| <u>customer number</u> | email address |


2. Define the relationship between entities.

The following is true:
- Each customer can have many orders.
- Each order can have only one customer.
- Orders can can have a number of lines.
- Each order line refers to an item

This yields the following relational model representation:

![relational model example diagram](/img/example_relational_model.png)

---

## Practice

Refer to [practice one](/practice/01.pdf) for details.
