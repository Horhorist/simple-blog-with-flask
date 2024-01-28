It saves the posts as markdown. Newly written posts are saved under the markdown folder. No need for a password. You just need to keep the url of the typed part hidden. It is enough to keep the url of the area to be written hidden. 

Just change the **nivis** in line 17 of the app.py file.

``@app.route('/nivis')

def admin():

    return render_template('admin.html')``
    
I will share the ability to delete and edit posts in the near future.

![image](https://github.com/Horhorist/simple-blog-with-flask/assets/109848153/77d7eacf-ebc4-4c4d-84d1-b16a7465344e)

