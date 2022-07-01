ETHAN BROWN 101031125, NIMA DADAR 100898748

OS Developed On: Windows 10
Browser Test On: Google Chrome

To install node_modules:
npm install

To run server:
npm test

Accessing the server at:
http://127.0.0.1:3000/index.html
http://127.0.0.1:3000/find



The line reader works by taking an input file(the xml file), and reading it line by line.
It then looks for opening tags, then stores all the data in a temp array after the tag until the closing iteration of this tag. The only tag that is slightly different is
the recipe tag. When it reaches an opening recipe tag it starts a new recipe. When it reaches a closing recipe tag, it pushes the recipe to the temp array.
Once it reaches the end of the file it pushes all the recipes to an SQLite database. It does this using npm sqlite3 functions.