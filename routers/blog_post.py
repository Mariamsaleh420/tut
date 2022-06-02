from typing import Optional
from fastapi import APIRouter ,Query ,Path, Body
from pydantic import BaseModel

router = APIRouter(

prefix = '/blog',
tags = ['blog']

)
class BlogModel(BaseModel):
    #TYPE OF DATA THAT i want to receive from creat_blog
    #to acheive that i want to have a prameter
    # that is passed through our function blog: BLOgmodel
    title: str
    content: str
    no_comments: int
    published: Optional[bool]
   
@router.post('/new/{id}')
def Creat_blog(blog: BlogModel, id :int, version:int =1):
    return {
        'id':id,
        'data': blog,
        'version': version
    }

@router.post('/new/{id}/comment')
def comment_creat(blog: BlogModel, id: int,
            comment_id: int = Query(None,
                  titel='id of the comment',
                  descreption = 'some description for comment_id',
                  deprecated=True,
                  alias= 'COMMENTID'
        )
    ):
    return {
        'blog':blog,
        'id':id,
        'comment_id':comment_id
    }
