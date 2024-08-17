from sqlmodel import Field, SQLModel


# table=True tells SQLModel that this is a table model
# without it, it would only be a data model
class Hero(SQLModel, table=True):
    # the id is aways required in the database and it will be
    # generated by the database (not by our code), so that's
    # why it's hinted as optional (int | None)
    id: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    # when hinting a field as optional, we tell SQLModel that
    # said field is not required when validating the data and that
    # it has a default value of none (null for most databases)
    age: int | None = None
