# What is a database?

A database is a collection of related data that:
- Represents some fact(s) about the real world
- is *logically coherent* with some inherent meaning
- has been designed and built with some purpose in mind

***

## Database Management Systems

A Database Management System (DBMS) is a collection of programs that facilitate
the process of defining, constructing, manipulating and sharing a database:

#### Defining

Specifying data types, structures and constraints of the data to be stored. The
definition is stored in the form of meta-data - a database catalog or
dictionary.

#### Constructing

Storing the data on some physical storage medium according to the definition,
controlled by the DBMS

#### Manipulating

The DBMS provides functions to query, update, add or alter data.

#### Sharing

The DBMS provides a framework for multiple users to manipulate data
simultaneously without causing conflicts.

***

## What does a DBMS look like?

#### Application programs

Queries, transactions or requests for data are managed by application programs.

#### Other important functions

- protecting the database from corruption or improper access/usage
- maintaining the database over the course of its lifetime


Ultimately, a general purpose DBMS is not strictly necessary - one could write
bespoke applications to serve the same purposes, i.e a *special purpose* DBMS.
Either way, the combination of a DBMS and a database is collectively referred to
as a *database system*.

---
## Databases vs. traditional file processing

### Traditional

- Each user defines, stores and implements the files necessary for their purposes, an
    approach resulting in redundancy. E.g an organisation might have different
    departments with separate files on individual customers.

### Database

- Their is a central repository of data - i.e. the database, that is defined
    once and then accessed by multiple users. This reduces storage needs and
    makes keeping data 'up to date' for all users a much simpler process. i.e an
    organisation with a database only needs to update the ADDRESS field once in
    order for this change to be reflected in the data accessible to all users.

---

Ultimately, the database approach has the following characteristics:

* the database is self-describing
* insulation between data and programs - data abstraction
* supports multiple and simultaneous access of data

## How is a database 'self-describing'?

The metadata of a DB describes the nature of data,
as well as the relationships between data.
In traditional file processing, individual applications manage the data
