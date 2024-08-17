# In this file i keep notes for functions that i couldn`t find in the documentation

- The Field() function allows you to specify database column properties such as default,

- While the whole application uses only one engine, a new session is createad for each group of operations with the database that belong togheter.
  - session = Session(engine) -> the session creates a new transaction and execute all the SQL code in that transaction that can be commited to the database with the sesssion.commit() function.
  - session.rollback() -> undo all the changes made in the session.
  - session.close() -> close the session.
  - session.add(object) -> add an object to the session.
