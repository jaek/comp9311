# The Entity-Relationship Model

The Entity Relationship (ER) model is a high-level conceptual data model.
In the ER system, the world is viewed as being made up of a collection of inter-related entities.
ER modeling is used as a design tool for the definition of databases.

ER has three major modeling constructs:

- **Entity** - collection of attributes describing an object
- **Attribute** - data item describing a property
- **Relationship** - association between entities
---
### Entities

Entities represent things which can *individually* exist in the real world.
- Entities can be *uniquely* identified.
- We can distinguish between an **entity** and an **entity-type**
- Entity types are a category (like a Class in OOP)
- Entities are instances of an entity type (like an Object in OOP)

### Keys and Foreign keys

- Entities may have any number of **superkeys**:
 a set of attributes which uniquely identifies an entity.
 - **Candidate keys** are minimal superkeys:
 no subset of a candidate key is a superkey itself.
- There can exist a number of possible candidate keys, for a given entity.
- One candidate key is selected by the DB designer as a **primary key**.
- If there is no set of attributes which can *uniquely* identify an entity,
it is a **weak entity**.
- Weak entities must have a **foreign key**. A foreign key is generally the primary key of an entity to which the weak entity is related.
- The **key constraint**:
In any extension of the entity type, there cannot be two entities having the same values for their key attributes.

### Attributes

Attributes describe *properties* of entities.
- Attributes may be **atomic** (single valued), **composite** or **multi-valued**.
- Composite - consists of a number of distinct values,
i.e (weight, height)
- Multi-valued - consists of a number of values of the same type,
i.e { email_address1, email_eddress2...}
- An attribute of an entity may have a NULL value.
- A *derived attribute* is an attribute whose value can be derived from other attributes/entities

### Drawing an ERD

Using the light rail example in [practice one](/practice/01.pdf):

#### 1 - Identify all entities in a system.

| Worker    |      |              |        |
| --------- | ---- | ------------ | ------ |
| worker_id | name | phone_number | salary |

| Team    |           |               |
| ------- | --------- | ------------- |
| team_id | team_name | member_number |

| Vehicle      |       |        |               |
| ------------ | ----- | ------ | ------------- |
| plate_number | model | colour | purchase_date |

| Order    |          |          |       |
| -------- | -------- | -------- | ----- |
| order_id | location | duration | price |


#### 2 - Relationship Matrix:

|         | Worker    | Team          | Vehicle   | Order    |
| ------- | --------- | ------------- | --------- | -------- |
| Worker  |           | leader/member | driver_of |          |
| Team    | works_for |               | owns      | works_on |
| Vehicle | driven_by | owned_by      |           |          |
| Order   |           | worked_by     |           |          |

#### 3 - Initial Diagram:

With the entities and relationships defined, we sketch a basic diagram:

![step_one](/notes/img/practice1_step1.png)

#### 4 - Describe cardinalities

![step_two](/notes/img/practice1_step2.png)

---
