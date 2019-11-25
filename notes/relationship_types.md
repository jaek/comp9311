# Relationship types

In the ER model, relationships are associations between two or more entities.
Relationships can be broken up into a number of sub-categories,
based on the nature of the relationship,
the role of the entities involved,
as the number of entities involved.

### Identifying relationship

In cases where a child entity cannot exist without a parent entity,
their relationship is referred to as an identifying relationship.
The child entity is a *weak entity* and can only be identified using both the parent primary key and its own attributes.
For example:

*Each chip manufacturer has several different flavours*

In this case, a database might represent each flavour as a child entity of BrandName:

![identifying relationship](/notes/img/identifying.png)

### Cardinality constraints

A **cardinality ratio constraint**:
specifies the number of relationship instances an entity can participate in.
These can be expressed in the format X:Y,
describing the number of entities of each entity type which can participate in the relationship.

### one-to-one

There is an exact 1-1 mapping between entities.
For example:

*There is one stationed at each firestation"*

![one to one relation](/notes/img/one_to_one.png)

### one-to-many

For each entity A, there may exist zero or more entities B.
Conversely, for each entity B there may exist only one entity A.
For example:

*Each school may have several teachers.
Each teacher may work at only one school.*

![one to many relationship](/notes/img/one_to_many.png)

Notice that the participation ratio of each entity is on the same side of the relationship as that entity.

### many to many

For each entity A, there may be zero or more entities B,
with the inverse also being true, i.e:

*A publication can have many Authors,
and each Author can have written several publications*

![many to many relationship](/notes/img/many_to_many.png)

### mandatory participation

**Mandatory/Total Participation** relationships are relationships in which one or more entities *must* be present.
In the ER model, this is represented with a double line, for example:

*An author may have written zero or more books,but each book has at least one author.*

![total participation](/notes/img/total_participation.png)
