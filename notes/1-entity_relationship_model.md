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
- A *derived attribute* is an attribute whose value can be derived from other attributes/entities.

### Relationships

[Relationships](/notes/relationships_types.md) capture how entities are related to one another.

- An entity type may be related to any number of other entity types.
- Each entity type that participates in a relationship plays a particular **role** in the relationship.
- Entities can play different roles in different relationships
or more than one role in one relationship.

- For example, an entity Person might be related to an entity Movie as either an actor or director:

![recursive ERD example](/notes/img/recursive_erd.png)

*The above relationship is described as a **recursive relationship**.*
- The **degree** of a relationship refers to the number of participating entity types.
- Relationships can have **cardinality constraints**,
which are rules that govern the number of individual entities which can participate in a relationship.

---

## Entity Relationship Diagrams

Entities and their relationships can be represented using an **Entity Relationship Diagram** (ERD).
