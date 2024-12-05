from fastapi import FastAPI, HTTPException, Request, Form
import uvicorn
from util import customization, model_loading
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
model_loading()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    tweet: str
    views: int
    bookmark_count: int
    favorite_count: int
    quote_count: int
    reply_count: int
    retweet_cout: int


@app.post("/predict")
async def predict(
        tweet: str = Form(...),
        views: int = Form(...),
        bookmark_count: int = Form(...),
        favorite_count: int = Form(...),
        quote_count: int = Form(...),
        reply_count: int = Form(...),
        retweet_count: int = Form(...)):
    try:
        data = {
            "tweet": tweet,
            "views": views,
            "bookmark_count": bookmark_count,
            "favorite_count": favorite_count,
            "quote_count": quote_count,
            "reply_count": reply_count,
            "retweet_count": retweet_count
        }
        print("Received data:", data)

        tweet = data.get("tweet")
        views = data.get("views")
        bookmark_count = data.get("bookmark_count")
        favorite_count = data.get("favorite_count")
        quote_count = data.get("quote_count")
        reply_count = data.get("reply_count")
        retweet_count = data.get("retweet_count")

        if None in [tweet, views, bookmark_count, favorite_count, quote_count, reply_count, retweet_count]:
            raise HTTPException(status_code=400, detail="Invalid input")

        result = customization(
            tweet,
            views,
            bookmark_count,
            favorite_count,
            quote_count,
            reply_count,
            retweet_count
        )

        print("Prediction result:", result)
        new_result = ""
        if bool(result[0]) == False:
            new_result = "Fact"
        else:
            new_result = "Rumor"

        return {"prediction": new_result}

    except Exception as e:
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.post("/predict2")
async def predict(item : Item):
    result = customization(
            tweet=item.tweet,
            views=item.views,
            bookmark_count=item.bookmark_count,
            favorite_count=item.favorite_count,
            quote_count=item.quote_count,
            reply_count=item.reply_count,
            retweet_count=item.retweet_cout
        )
    print("Prediction result:", result)
    new_result = ""
    if bool(result[0]) == False:
        new_result = "Fact"
    else:
        new_result = "Rumor"
    return {"prediction": new_result}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
