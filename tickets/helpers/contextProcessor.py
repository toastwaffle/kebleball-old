from tickets import app

@app.context_processor
def utility_processor():
    def get_all(query):
        return query.all()
    return dict(get_all=get_all)