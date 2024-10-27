# generated by fastapi-codegen:
#   filename:  creatures.oas.0.0.yaml
#   timestamp: 2024-10-27T07:09:28+00:00

from __future__ import annotations

from typing import List, Optional, Union

from fastapi import FastAPI

from models import Creature, Type

app = FastAPI(
    title='Creature Management API',
    version='1.0.0',
    description='A simple API to manage creatures.',
    servers=[{'url': 'http://localhost:3000/api'}],
)




@app.get('/creatures', response_model=List[Creature])
def get_creatures() -> List[Creature]:
    """
    Get a list of all creatures
    """
    # Initialize creature_list as an empty list
    creature_list: List[Creature] = []
    
    # Create a sample creature instance
    creature = Creature(id='1', name='Fenrir', type=Type.Werewolf, age=120)
    
    # Append the creature to the list
    creature_list.append(creature)
    
    # Return the list of creatures
    return creature_list


@app.post('/creatures', response_model=None, responses={'201': {'model': Creature}})
def post_creatures(body: Creature) -> Optional[Creature]:
    """
    Create a new creature
    """
    pass


@app.get('/creatures/{id}', response_model=Creature)
def get_creatures_id(id: str) -> Creature:
    """
    Get a creature by ID
    """
    pass


@app.put('/creatures/{id}', response_model=Creature)
def put_creatures_id(id: str, body: Creature = ...) -> Creature:
    """
    Update an existing creature
    """
    pass


@app.delete('/creatures/{id}', response_model=None)
def delete_creatures_id(id: str) -> None:
    """
    Delete a creature
    """
    pass
