from fastapi import FastAPI

app = FastAPI()

STORIES = [
    {'title': 'Title One', 'author': 'Author One', 'genre': 'Genre One'},
    {'title': 'Title Two', 'author': 'Author Two', 'genre': 'Genre Two'},
    {'title': 'Title Three', 'author': 'Author Three', 'genre': 'Genre Three'},
    {'title': 'Title Four', 'author': 'Author Four', 'genre': 'Genre Two'},
    {'title': 'Title Five', 'author': 'Author Two', 'genre': 'Genre One'}
]

# always have the smaller apis in the front because FastAPI goes from top to bottom while looking for APIs
@app.get("/stories")
async def get_all_stories():
    return STORIES

# query parameter
@app.get("/stories/")
async def get_all_stories(genre: str):
    stories_of_genre = []
    for story in STORIES:
        if story.get('genre').casefold() == genre.casefold():
            stories_of_genre.append(story)
    return stories_of_genre


# always have the static apis in the front because FastAPI goes from top to bottom while looking for APIs
@app.get("/stories/myStory")
async def get_favorite_story():
    return {"story": "My favourite story"}

# path parameter
# always have dyncamic params after smaller and static params
# user %20 to represent space in URLs
@app.get("/stories/{story_title}")
async def get_story(story_title: str):
    for story in STORIES:
        if story.get('title').casefold() == story_title.casefold():
            return story
        
# path parameter and query parameter 
# remember that adding the slash at the end of the path is important
@app.get("/stories/{story_author}/")
async def get_story(story_author: str, genre: str):
    filtered_stories = []
    for story in STORIES:
        if story.get('author').casefold() == story_author.casefold() and \
            story.get('genre').casefold() == genre.casefold():
            filtered_stories.append(story)
    return filtered_stories
        

