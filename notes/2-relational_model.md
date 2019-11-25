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
