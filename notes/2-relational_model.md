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


**Referential integrity**: The value of *FK* must occur in *R<sub>2</sub>*
**OR** be entirely NULL

### Integrity constraints


With these definitions, we can describe a **relational database schema** as:
* a set of relation/table schema {*R<sub>1</sub>*, *R<sub>2</sub>*, *R<sub>3</sub>*...}*R<sub>n</sub>*
* a set of integrity constraints which ensure the uniformity of the database:

    * Entity constraints - no attribute of a primary key can be null.
    * Key constraints - no two tuples of a relation can share the same primary key.
    * Referential constraints - if *R<sub>1</sub>* has a foreign key *FK* referring to  *R<sub>2</sub>*, tuples of *R<sub>1</sub>* must either be NULL or exist as a value in *R<sub>2</sub>*.
    * Domain constraints - attributes of must fall within the specified domain.
---

## Representing the relational model

Drawing a relational model representation of a database consists of a number of steps.
Taking the example of a simple database for an online shop:
The online shop must keep track of customers,
as well as the weight and contents of their orders.

---

## Practice

Refer to [practice one](/practice/01.pdf) and [entity relationship models](/notes/1-entity_relationship_modles.md) for details on ER representation.

Using this ER diagram, describing the organisation of a construction company, we will describe a relational model.

![er diagram](/notes/img/practice1_step2.png)

1. For each regular entity *E* in the ERD,
create a relation with the same  **simple** attributes.
Then select a primary key from the candidate keys for *E*:

| Worker           |        |      |              |
| ---------------- | ------ | ---- | ------------ |
| <u>worker_id</u> | salary | name | phone_number |

| Team           |           |               |
| -------------- | --------- | ------------- |
| <u>team_id</u> | team_name | member_number |

| Order    |          |          |       |
| -------- | -------- | -------- | ----- |
| order_id | duration | location | price |

| Vehicle             |        |       |               |
| ------------------- | ------ | ----- | ------------- |
| <u>plate_number</u> | colour | model | purchase_date |


2. For each weak entity type *W*, create a new relatio,n *R* with:
    *  All simple attributes (and simple components of composite attributes) of W,
    and include as a foreign key the prime attributes of the relation derived from E.
    * The foreign key plus the partial key of W.

This ERD does not feature any weak entity types. As an example:

![weak entity relationship](/notes/img/weak_example.png)

| Flavour                |             |        |
| ---------------------- | ----------- | ------ |
| <u>manufacturer id</u> | <u>name</u> | colour |

3. For each 1:1 relationship *X* between relations *A* and *B*:
    * Choose one relation - e.g *A*
    * Add the attributes of the primary key of *B* to *A* as a foreign key
    * Add the attributes of *X* to *A*

| Worker           |        |      |              |
| ---------------- | ------ | ---- | ------------ |
| <u>worker_id</u> | salary | name | phone_number |

| Team           |           |               |
| -------------- | --------- | ------------- |
| <u>team_id</u> | team_name | member_number |

becomes:

| Team           |            |           |               |
| -------------- | ---------- | --------- | ------------- |
| <u>team_id</u> | manager_id | team_name | member_number |


4. For each 1:N relationship *X* between *A* and *B*, e.g *Team* and *Worker*:

* Add the attribute of the primary key of *A* to *B* as a foreign key.

| Worker           |        |      |              |         |
| ---------------- | ------ | ---- | ------------ | ------- |
| <u>worker_id</u> | salary | name | phone_number | team_id |


* Add any simple attributes of *X* to *B*.

For example, if the relation ````member_of```` had an attribute ````start_date````:

| Worker           |        |      |              |         |            |
| ---------------- | ------ | ---- | ------------ | ------- | ---------- |
| <u>worker_id</u> | salary | name | phone_number | team_id | start_date |


5. For each M:N relationship *X* between entities *A* and *B*,
create a new relation *R*.
Give *R* the the keys of *A* and *B* as foreign keys, as well as the simple attributes of *X*.

For example, the relation ````driver_of```` between ````Worker```` and ````Vehicle````:

![converting an m to n relationship to relational](/notes/img/practise1_step3.png)

| Driver           |                     |                   |
| ---------------- | ------------------- | ----------------- |
| <u>worker_id</u> | <u>plate_number</u> | kilometers_driven |

6. For each multivalued attribute *A* of relation *R*,
create a new relation *R<sub>2</sub>* with the following attributes:
    * *A*, with the key of *E* as a foreign key.
    * All attributes of *R<sub>2</sub>* as the primary key.

![weak entity relationship](/notes/img/weak_example.png)

| Allergens_list         |             |                 |
| ---------------------- | ----------- | --------------- |
| <u>manufacturer id</u> | <u>name</u> | <u>allergen</u> |

7. For each n-ary relationship *R* bewtween relations *A* and *B*,
create a new relation with:
    * The the keys of *A* and *B* as foreign keys,
     as well as the simple attributes of *X*.
     * If one of the relationships is N=1, use that relations primary key as primary key for the new relation:

---

This process yields the following Relational Model Representation:

| Order    |          |          |       |
| -------- | -------- | -------- | ----- |
| order_id | duration | location | price |

| Team           |            |           |               |
| -------------- | ---------- | --------- | ------------- |
| <u>team_id</u> | manager_id | team_name | member_number |

| Worker           |        |      |              |         |            |
| ---------------- | ------ | ---- | ------------ | ------- | ---------- |
| <u>worker_id</u> | salary | name | phone_number | team_id | start_date |

| Driver           |                     |                   |
| ---------------- | ------------------- | ----------------- |
| <u>worker_id</u> | <u>plate_number</u> | kilometers_driven |

| Vehicle             |        |       |               |
| ------------------- | ------ | ----- | ------------- |
| <u>plate_number</u> | colour | model | purchase_date |

With the relationships:

| source | destination |
| ------ | ----------- |
| team   | order       |
| team   | worker      |
| worker | team        |
| driver | worker      |
| driver | vehicle     |

#### Question 6 - Cardinality Ratios

| Entity 1     | Cardinality Ratio | Entity 2             |
| ------------ | ----------------- | -------------------- |
| Student      | 1:N               | SocialSecurityNumber |
| Student      | N:M               | Teacher              |
| Classroom    | N:M               | Wall                 |
| Country      | 1:1               | CurrentPresident     |
| Course       | N:M               | Textbook             |
| Item         | N:1               | Order                |
| Student      | N:M               | Class                |
| Instructor   | 1:1               | Office               |
| auction_item | 1:N               | auction_bid          |
