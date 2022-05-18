const express = require('express')
const app = express()
const port = 3000
app.set('view engine', 'jade')

app.get('/', (req, res) => {
  res.render('home', {title: 'Hello', names: [
	  'button1', 
	  'button2', 
	  'button3', 
	  'button4', 
	  'button5', 
	  'button6', 
	  'button7', 
	  ]})
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
