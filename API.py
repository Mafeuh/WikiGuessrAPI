import WikiGetter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def root():
    return { 'ok': 1 }


@app.get("/getpage")
def get_page():
    json = WikiGetter.get_random_page()

    return json


@app.get("/getpage/{theme}")
def get_page_by_theme(theme: str):
    json = WikiGetter.get_random_page(theme)
    return json


@app.get("/getcategories")
def get_categories():
    return WikiGetter.CATEGORIES