from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for posts and comments (for simplicity, we'll use lists)
posts = []

# Home page to display posts and form to create new post
@app.route('/')
def index():
    return render_template('index.html', posts=posts)

# Route to handle new post submission
@app.route('/add_post', methods=['POST'])
def add_post():
    if request.method == 'POST':
        user = request.form['user']
        content = request.form['content']
        # Append new post to the posts list
        posts.append({'user': user, 'content': content, 'comments': []})
    return redirect(url_for('index'))

# Route to handle comment submission
@app.route('/add_comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    if request.method == 'POST':
        user = request.form['user']
        comment = request.form['comment']
        # Add comment to the appropriate post
        posts[post_id]['comments'].append({'user': user, 'comment': comment})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

