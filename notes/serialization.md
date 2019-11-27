# Serialization

### Serial Schedules

A serial schedule does not interleave transactions.



Practice Exam Q5 C):

|     | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T1  |     |     |     | rX  | wX  | wZ  |     |     | rY  | wy  |     |     |     |
| T2  | rY  | wY  |     |     |     |     |     | rX  |     |     | wX  |     |     |
| T3  |     |     | rY  |     |     |     | wY  |     |     |     |     | rW  | wW  |

The following conflicts occur:

| source | dest               |
| ------ | ------------------ |
| 2rY    | 3wY, 1wY           |
| 2wY    | 3rY, 3wY, 1rY, 1wY |
| 3rY    | 1wY                |
| 1rX    | 2wX                |
| 1wX    | 2rX, 2wX           |
| 3wY    | 1rY                |

Yielding the following conflict graph:

![graph](/notes/img/exam_graph.png)

Given that the graph contains cycles, it is **not** conflict serializable.
