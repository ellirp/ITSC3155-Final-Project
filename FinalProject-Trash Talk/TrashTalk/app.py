from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# initialize an empty list of posts
posts = []
#initialize an empty dictionary of comments for each post
comments = {}

@app.route('/')
def home():
    # pass the list of posts and comments to index.html
    return render_template('index.html', posts=posts, comments=comments)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # get text of new post and username from submission
        post_text = request.form['post-text']
        username = request.form['username']
        # add the new post and username to the list of posts
        posts.append({'text': post_text, 'username': username})
        # empty list of comments is created for the new post
        comments[post_text] = []
        # back to the home page
        return redirect('/')
    else:
        # if GET, render the post.html template
        return render_template('post.html')

@app.route('/comment/<post_text>', methods=['GET', 'POST'])
def comment(post_text):
    if request.method == 'POST':
        # get the text of the new comment and username from the form
        comment_text = request.form['comment-text']
        username = request.form['username']
        # add comment + username to list of comments for the post
        comments[post_text].append({'text': comment_text, 'username': username})
        # back to the home page
        return redirect('/')
    else:
        # if GET, render the comment.html template
        return render_template('comment.html', post_text=post_text)

if __name__ == '__main__':
    app.run(debug=True)

