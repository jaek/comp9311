# The Relational Model

Entity A   | -
---------- | -----------
Attribute1 | Attribute 2

&nbsp;&nbsp;&nbsp;&nbsp;⭥⭥⭥⭥⭥⭥

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⭥relation⭥

&nbsp;&nbsp;&nbsp;&nbsp;⭥⭥⭥⭥⭥⭥

Attribute1 | Attribute3
---------- | ----------
Entity B   | -

*Entity A is related to entity B because they share attribute 1*

---

## Represting the relational model

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
