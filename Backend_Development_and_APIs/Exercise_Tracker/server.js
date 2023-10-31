//dependencies
const express = require('express')
const app = express()
const cors = require('cors')
require('dotenv').config()
const mongoose = require('mongoose');
const connection_uri = process.env['MONGO_URI'];
const bodyParser = require('body-parser')
//db
mongoose.connect(connection_uri)
//schemas
const User = require('./models/userModel.js');
const Exercise = require('./models/exerciseModel.js');
//body parser
app.use(bodyParser.urlencoded({
  extended: false
}));
app.use(bodyParser.json());

//post route/users

app.post('/api/users',(req,res) => {
  //create user

  const newUser = new User({
    username: req.body.username
  })
  newUser.save((err, data) => {
    if(err || !data) {
      res.send("an error has ocurred")
    } else {
      res.json(data)
    }
  })
})

app.post('/api/users/:id/exercises', (req,res) => {
  const id = req.params.id;
  const {description, duration,date} = req.body;

  User.findById(id ,(err ,userData) => {
    if(err || !userData) {
      res.send('couldnt find user')
    } else {
      const newExercise = new Exercise({
          userId: id,
          description,
          duration,
          date: new Date(date),
      });
      newExercise.save((err, data) => {
        if(err||!data) {
          res.send('an error saving this')
        } else {
          const {description, duration,date, _id} = data;
          res.json({
            username: userData.username,
            description,
            duration,
            date: date.toDateString(),
            _id: userData.id
          })
        }
      })
    }
  })
})

//get routes

app.get('/api/users/:id/logs',(req,res) => {
  const { from, to , limit } = req.query;
  const {id} = req.params;
    User.findById(id ,(err ,userData) => {
      if(err || !userData) {
        res.send('couldnt find user')
      } else {
          let dateObj = {}
          if(from){
            dateObj['$gte'] = new Date(from)
          }

          if(to) {
            dateObj['$lte'] = new Date(to)
          }
        
          let filter = {
            userId: id
          }
          if (from || to) {
            filter.date = dateObj
          }
          let nonNullLimit = (limit !== null && limit !== undefined) ? limit : 500;
        
          Exercise.find(filter).limit(nonNullLimit).exec((err,data) => {
            if(err || !data) {
              res.json([])
            } else {
              const count = data.length;
              const rawLog = data;
              const { username, _id} = userData;
              const log = rawLog.map((l) => ({
                description: l.description,
                duration: l.duration,
                date: l.date.toDateString()
              }))
              res.json({username, count, _id, log})
            }
          })

        
      }
    })
})

app.get('/api/users', (req,res) => {
  User.find({}, (err,data) => {
    if(!data) {
      res.send('no data found')
    } else {
      res.json(data)
    }
  })
})


//static files
app.use(cors())
app.use(express.static('public'))
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/index.html')
});


//server
const listener = app.listen(process.env.PORT || 3000, () => {
  console.log('Your app is listening on port ' + listener.address().port)
})
