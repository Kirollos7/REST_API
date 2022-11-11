from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List
from models.article import Article
from models.shelf import Shelf
from models.warehouse import Warehouse


app = FastAPI()

root_body = '''
            <div style="text-align:center;font-family:Arial;">
                <h1 style="color:8A2BE2;"> Metro Market </h1>
                <p>Coding Challenge: Build a REST API with Python</p>
                <br></br>
                <br></br>
                <div >
                    <a style="color:#FFA500;" href="http://localhost:8000/docs">  
                        API DOC
                    </a>
                    <br></br>
                    <a style="color:#FFA500;" href="http://localhost:8000/api/articles">  
                        Get Articles
                    </a>
                    <br></br>
                    <a style="color:#FFA500;" href="http://localhost:8000/api/shelfs">  
                        Get Shelfs
                    </a>
                    <br></br>
                    <a style="color:#FFA500;" href="http://localhost:8000/api/warehouse">  
                        Get Warehouse
                    </a>
                </div>
                <footer style=" position: absolute;bottom: 0;width: 100%;height: 2.5rem;">
                    By: Kirollos Noshy
                </footer>
            <div>
            '''

notfound = '''
            <div style="text-align:center; text-familt:Arial;color:orange;">
                Not Found...
                <br></br>
                please go back and try again.
                <br></br>
                <a href="http://localhost:8000/">  
                 <button>Home</button>
                </a>
            </div>
            
        '''

@app.get("/")
async def root():
    return HTMLResponse(content=root_body, status_code=200)

@app.get("/notfoundpage")
def not_found_page():
    return HTMLResponse(content=notfound, status_code=200)


# ------------------------------------------------------------------------------------
# *** Articles HTTP Methods *** #

# Database 3 records
db: List[Article] = [
    Article(
        id=1,
        name="Artical 1",
        description="Starter-Set in charcoal with two pods."
    ),
    Article(
        id=2,
        name="Artical 2",
        description="This is the second artical."
    ),
    Article(
        id=3,
        name="Artical 3",
        description="This is the third artical."
    )
]

# GET method ---> retrieve all data
@app.get("/api/articles")
async def fetch_articles():
    return db


# GET method ---> retrieve one record b ID 
@app.get("/api/articles/{id}")
async def fetch_one_article(id: int):
    try:
        return db[id-1]
    except:
        return not_found_page()


# CREATE method
@app.post("/api/articles")
async def create_article(articel: Article):
    db.append(articel)
    return {"id": articel.id}

# DELETE method
@app.delete("/api/articles/{article_id}")
async def delete_article(article_id: int):
    for article in db:
        if article.id == article_id:
            db.remove(article)
    return {"Deleted Article": article_id}
        
# UPDATE method
@app.put("/api/articles/{article_id}/update/{description}")
async def update_article(article_id: int, description:str):
    for article in db:
        if article.id == article_id:
            article.description = description
    return {"Update Article": article_id, "Description": description}

# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# # *** Shelfs HTTP Methods *** #
shelf_db: List[Shelf] = [
    Shelf(
        row=1,
        bay=1,
        height=1.2,
        width=2.5,
        depth=5.5
    ),
    Shelf(
        row=1,
        bay=2,
        height=9,
        width=5.4,
        depth=3.6
    ),  
]

# GET method ---> retrieve all data
@app.get('/api/shelfs')
async def fetch_shelfs():
    return shelf_db
# ***



# Shelf with all properties
@app.get('/api/shelfs/{row}/{bay}')
async def fetch_one_shelfs(row: int, bay: int):
    for shelf in shelf_db:
        if shelf.row == row and shelf.bay == bay:
            dic = dict(shelf)
            dic.pop('row')
            dic.pop('bay')
            return dic
        
# CREATE method
@app.post("/api/shelfs")
async def create_shelf(shelf: Shelf):
    shelf_db.append(shelf_db)
    return {
            "row": shelf.row,
            "bay": shelf.bay,
            "height": shelf.height,
            "width": shelf.width,
            "depth": shelf.depth
            }


# DELETE method
@app.delete("/api/shelfs/{row}/{bay}")
async def delete_shelf(shelf_row: int, shelf_bay: int):
    for shelf in shelf_db:
        if shelf.row == shelf_row and shelf.bay == shelf_bay:
            shelf_db.remove(shelf)
    return {"Deleted Shelf row": shelf_row}
        
# UPDATE method
@app.put("/api/shelfs/{row}/{bay}/update/{depth}")
async def update_shelf(row: int, bay: int, depth: float):
    for shelf in shelf_db:
        if shelf.row == row and shelf.bay == bay:
            shelf.depth = depth
    return {"Update Shelf row": row, "Depth": depth}

# -----------------------------------------------------------------------------------



# -----------------------------------------------------------------------------------
# # *** Warehouse HTTP Methods *** #


Article_DB: List[Warehouse] = [
    Warehouse(
        id=db[0],
        amount=50
    ),
    Warehouse(
        id=db[1],
        amount=100
    )
]

# GET method ---> retrieve all data
@app.get('/api/warehouse')
async def fetch_warehouse():
    return  Article_DB



# Search stored articles with the help of the URL parameters row, bay and id in


@app.get('/api/warehouse?{row}&{bay}&{id}')
async def fetch_special_warehouse(row: int, bay: int , id: int):
    for rec in db:
        if rec.id == id:
            for i in shelf_db:
                if i.row == row and i.bay == bay:
                    return db, shelf_db










# -----------------------------------------------------------------------------------



