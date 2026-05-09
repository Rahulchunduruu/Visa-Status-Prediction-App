from pydantic import BaseModel,Field
from typing import Annotated,Literal


class Item(BaseModel):
    age:Annotated[int,Field(...,gt=20,lt=80,description='Age of the user')]
    height:Annotated[float, Field(..., gt=0, description='height of the user')]
    Degree:Annotated[Literal['Graduate','Post Graduate','No Degree'], Field(..., description='Educational Qualification of the user')]
    workexperience:Annotated[int, Field(..., ge=0, description='work experience of the user')]
    income_lpa:Annotated[int,Field(...,ge=0,description='Annual Salary interms of Lakhs')]
    crimerecord:Annotated[Literal['yes','no'],Field( ..., description='any criminal record of the user' )]
    city:Annotated[Literal["Visakhapatnam", "Itanagar", "Guwahati", "Patna", "Raipur", "Panaji", "Ahmedabad", "Gurugram", "Shimla", "Ranchi", "Bengaluru", "Kochi", "Indore", "Mumbai", "Imphal", "Shillong", "Aizawl", "Kohima", "Bhubaneswar", "Ludhiana", "Jaipur", "Gangtok", "Chennai", "Hyderabad", "Agartala", "Lucknow", "Dehradun", "Kolkata"],Field(...,description='Name of the city belongs to')]
    Nationality:Annotated[Literal['INDIAN','NOT INDIAN'],Field(...,description='country he belongs to')]
  