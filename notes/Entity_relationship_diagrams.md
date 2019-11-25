# Drawing ER diagrams

The world is viewed as being made up of a collection of inter-related entities.

ER has three major modeling constructs:

- **Entity** - collection of attributes describing an object
- **Attribute** - data item describing a property
- **Relationship** - association between entities
---

Entity A   | -
---------- | -----------
Attribute1 | Attribute 2

&nbsp;&nbsp;&nbsp;&nbsp;⭥⭥⭥⭥⭥⭥⭥

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⭥relation⭥

&nbsp;&nbsp;&nbsp;&nbsp;⭥⭥⭥⭥⭥⭥⭥

Attribute1 | Attribute3
---------- | ----------
Entity B   | -

*Entity A is related to entity B because they share attribute 1*

---
### Entities

Entities represent things which can *individually* exist in the real world.
- Entities can be *uniquely* identified.
- We can distinguish between an **entity** and an **entity-type**
- Entity types are a category (like a Class in OOP)
- Entities are instances of an entity type (like an Object in OOP)
- Entities may have a **key**: a set of attributes which uniquely identifies an entity.
- If there is no set of attributes which can *uniquely* identify an entity,
it is a **weak entity**.
- Weak entities must have a **foreign key**. A foreign key is generally the primary key of an entity to which the weak entity is related.

### Attributes

Attributes describe *properties* of entities.
- Attributes may be single valued (atomic) or multi-valued.
- An attribute may also have a NULL value.
- A *derived attribute* is an attribute whose value can be derived from other attributes/entities.

### Relationships

- Relationships capture how entities are related to one another.
- In the ER model, relationships can have attributes.

## Cheatsheet

- Keys are indicated by underlining.
- Composite attributes use () - composite: attribute consists of a number of attributes
- Multivalued attributes use {} - multivalued: there may be any number of possible elements to this attribute
