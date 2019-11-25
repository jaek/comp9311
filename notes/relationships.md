# ERD notation

## Entity types

### Weak Entity

A weak entity cannot be uniquely identified by its attributes alone. It must use
a foreign key in conjunction with its attributes to create a primary key.

### Identifying relationship

In cases where a child entity cannot exist without a parent entity, their
relationship is referred to as an identifying relationship. The child entity is
a "weak entity" and can only be identified using both the parent primary key and
its own attributes.

### Composite attribute

An attribute consisting of a number of sub-attributes - i.e address consists of
street name, street number, postcode, etc. These sub-attributes might be of
different types, e.g street_number = int, street_name = string, postcode = int
(4 numbers), etc

### Multivalued attribute

An attribute which can *contain* multiple values of the same type. For example,
an employee might have zero, one or multiple phone numbers. Unlike composite
attributes, all values are of the same type.

## Relation types

### one to one

There is an exact 1-1 mapping between entities. If we are only concerned with
the vehicle that a person is *currently* driving, we might describe the
relationship thusly:

[person]--1--<drives>--1--[vehicle]

### one to many

One customer might have zero or more orders, but each order can only have one
customer.

[Customer]--1--<places>--n--[order]
[Rider]--1--<delivers>--n--[order]

### many to many

A student might take zero or more courses, and each course might have zero or
more students.


[course]--m--<enrolled_in>--n--[student]

### mandatory participation

An author may have written zero or more books, but each book has at least one
author.

[book]--m--<written_by>==n==[author]

### optional participation
