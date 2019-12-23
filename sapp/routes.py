from YoutubeSearch import app
from YoutubeSearch.Search import main

@app.route('/')
@app.route('/index')
def index():
	return main()