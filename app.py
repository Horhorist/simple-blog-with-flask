# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
import markdown

app = Flask(__name__)

# Markdown dosyalarının bulunduğu klasör
markdown_folder = 'markdown/'

@app.route('/')
def index():
    posts = get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/nivis')
def admin():
    return render_template('admin.html')

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')

    if title and content:
        save_post(title, content)
    
    return redirect(url_for('admin'))

@app.route('/delete_post/<title>')
def delete_post(title):
    delete_post_by_title(title)
    return redirect(url_for('admin'))

def get_all_posts():
    posts = []
    for filename in os.listdir(markdown_folder):
        if filename.endswith('.md'):
            filepath = os.path.join(markdown_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                html_content = markdown.markdown(content)
                posts.append({'title': filename[:-3], 'content': html_content, 'date': get_post_date(filepath)})
    return sorted(posts, key=lambda x: x['date'], reverse=True)

def save_post(title, content):
    filename = title.lower().replace('_', ' ') + '.md'
    filepath = os.path.join(markdown_folder, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def delete_post_by_title(title):
    filename = title.lower().replace('_', ' ') + '.md'
    filepath = os.path.join(markdown_folder, filename)
    if os.path.exists(filepath):
        os.remove(filepath)



def get_post_date(filepath):
    return datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)
