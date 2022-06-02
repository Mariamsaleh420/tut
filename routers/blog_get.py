from typing import Optional
from fastapi import APIRouter 
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags= {'blog'}
)

@router.get('/all',

summary= 'retreive all blogs',
description ='this api call simulates fething all blogs.')
def get_all_blogs(page, pagesize: Optional[int] = None):
    return {'message': f'all {pagesize} blogs on page {page}'}

@router.get('/{id}/comment/{comment_id} ')
def get_comment(id : int , comment_id:int, valid: bool=True, username:  Optional[str]=None):
    
    """
    dfgner
    """
    return {'message': f'blog_id {id}, comment_id {comment_id},valid {valid},username {username}'}

class blog_type(str, Enum):
    short:'short'
    story:'story'
    howto:'howto'

@router.get('/type/{type}')
def get_blog_type(type =blog_type):
    return {'message': f'blog type {type}'}

@router.get('/{id}')
def get_blog(id):
    return {'message': f'blog with id {id}'}
