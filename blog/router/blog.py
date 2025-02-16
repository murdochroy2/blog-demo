from fastapi import APIRouter, HTTPException, status, Depends
from blog import schemas, models, database, repository, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(prefix='/blog',tags=['Blogs'])

get_db = database.get_db

@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = blog.create(request, db)
    return new_blog

@router.get('', response_model=list[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = blog.get_all(db)
    return blogs

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.show(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)