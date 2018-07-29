let sqlite = require('sqlite3').verbose();
let db = new sqlite.Database('/Users/ianrigg/workspace/python/reddit-browser/database.db');

var express = require('express');
var api = express();

api.get('/posts', function(req, res) {
    db.get("SELECT * FROM posts", function(err, row) {
        res.json({ "posts" : row.value});
    });
});

api.listen(3000);
