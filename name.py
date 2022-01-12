from flask import Flask,jsonify,request
from storage import all_articles,liked_articles, not_liked_articles, did_not_watch
from demographicfiltering import output
from contentfiltering import get_recommandations
app=Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    }),

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),

@app.route("/unliked-articles",methods=["POST"])
def unliked_article():
    article=all_articles[0]
    not_liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),

@app.route("/did-not-watch",methods=["POST"])
def did_not_watch():
    article=all_articles[0]
    did_not_watch.append(article)
    return jsonify({
        "status":"success"
    }),
@app.route("/recommanded-movie")
def recommanded_movie():
    all_recommanded=[]
    for liked_movie in liked_articles:
        output=get_recommandations(liked_movie[19])
        for data in output:
            all_recommanded.append(data)
    import itertools
    all_recommanded.sort()
    all_recommanded=list(all_recommanded for all_recommanded, _ in itertools.groupby(all_recommanded))
    movie_data=[]
    for recommanded in all_recommanded:
        _d={
            "title":recommanded[0],
            "release_date":recommanded[1],
            "duration":recommanded[2],
            "rating":recommanded[3],
            "overview":recommanded[4]
        }
        movie_data.append(_d)
    return jsonify({
         "data": movie_data,
         "status": "success"
    })

if __name__ == "__main__":
    app.run()