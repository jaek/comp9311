## one to one

[entity A]---1---<relationship>---1---[Entity B]

## one to many

Only one instance of entity *A* can be associated with entity *B*

[Entity A]---1---<relationship>---N---[Entity B]

## many to one

More than one instance of entity *A* can be associated with entity *B*, 
but only one instance of entity *B* can be associated with entity *A*

"Each driver can have a number of orders, but each order must have only one
driver"

[Order]---N---<delivered_by>---1---[Driver]
[Entity A]---N---<Relationship>---1---[Entity B]
