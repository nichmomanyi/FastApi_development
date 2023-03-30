
from .. import schemas, utils, models, oauth2
from fastapi import FastAPI, Response,status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db

router=APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts=cursor.fetchall()
    posts=db.query(models.Post).all()
    return posts 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    
    print (current_user.email)
    #new_post=models.Post(title=post.title, content=post.content, published=post.published)
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()   
    db.refresh(new_post)
    
    return new_post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id= %s""", str((id),))
    # test_post=cursor.fetchone()
    # post=find_post(id) 
    test_post=db.query(models.Post).filter(models.Post.id == id).first()
    if not test_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Message:ID number {id} does not exist")
    return test_post
    
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post (id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id= %s RETURNING * """,str((id),))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    deleted_post=db.query(models.Post).filter(models.Post.id == id)
    
    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id {id} does not exist")
    deleted_post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post (id: int, updatedpost:schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts  SET title= %s, content= %s, published= %s WHERE id=%s RETURNING * """,(post.title, post.content, post.published, str((id),)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    
    updated_post=db.query(models.Post).filter(models.Post.id==id)
    post=updated_post.first()
    
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id {id} does not exist")
    
    # updated_post.update({'title':'This is my best lesson of study', 'content':'I just love API'},synchronize_session=False)
    updated_post.update(updatedpost.dict(),synchronize_session=False)

    db.commit()
    return updated_post.first()