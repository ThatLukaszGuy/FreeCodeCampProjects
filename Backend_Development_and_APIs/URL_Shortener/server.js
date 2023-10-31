const connection_url = process.env['MONGO_URI']
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const app = express();
const mongoose = require('mongoose')
const bodyParser = require('body-parser')
const dns = require('dns')
const urlparser = require('url')
// Basic Configuration
const port = process.env.PORT || 3000;

//db
app.use(bodyParser.urlencoded({extended: false}))

mongoose.connect(connection_url)

const UrlSchema = mongoose.Schema({
  url: String
});
const Url = mongoose.model('Url', UrlSchema);


app.use(cors());

app.use('/public', express.static(`${process.cwd()}/public`));

app.get('/', function(req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// Your first API endpoint
app.get('/api/hello', function(req, res) {
  res.json({ greeting: 'hello API' });
});

//post

app.post('/api/shorturl', (req, res) => {
  const bodyUrl = req.body.url;

  const thing = dns.lookup(urlparser.parse(bodyUrl).hostname, (error, address) => {
    if(!address) {
      res.json({ error: "Invalid URL"})
    } else {
      const URL = new Url({ url: bodyUrl })

      URL.save((err, data) => {
        res.json({
          original_url : data.url,
          short_url : data.id
          
        })
      })
    }
  })
})

app.get('/api/shorturl/:id',(req,res) => {
  const id = req.params.id;
  Url.findById(id, (err, data) => {
    if(!data) {
      res.json({error: "Invalid URL"})
    } else {

      res.redirect(data.url)
    }
  })
})



app.listen(port, function() {
  console.log(`Listening on port ${port}`);
});
