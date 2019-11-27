/* housekeeping */
DROP SCHEMA IF EXISTS test_schema;
DROP TABLE IF EXISTS real_number_types;
DROP TABLE IF EXISTS basic_number_types;
DROP TABLE IF EXISTS date_and_time;
DROP TABLE IF EXISTS char_types;
/* Create a new schema */
CREATE SCHEMA test_schema;

/* PostgreSQL has four basic numeric types */
--Integer types can be 2, 4 or 6 byte
CREATE TABLE basic_number_types
(
  _6_byte_int BIGINT,
  _4_byte_int INTEGER,
  _2_byte_int SMALLINT,
  decimal_integer NUMERIC(4,0)
);

/* As well as two floating point types */
CREATE TABLE real_number_types
(
  small_real REAL,
  big_real DOUBLE PRECISION
);

/* There are a number of different types for storing date and time */
CREATE TABLE date_and_time
(
  _date DATE,
  _time TIME,
  _interval INTERVAL,
  time_stamp TIMESTAMP
);

/* There are three basic types for strings */
CREATE TABLE char_types
(
  some_text text,            -- variable unlimited length
  up_to_20  varchar(20),    -- Variable Length, up to 20 characters
  up_to_100 varchar(100),
  always_20 char(20)       -- Fixed length, up to 20 characters, padded with whitespace
);

/* The type system is the most basic form of domain constraint */
