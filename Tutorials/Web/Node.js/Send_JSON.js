const express = require('express');
const path = require('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {

    // This should not be prefered as it has to detect the content to send as JSON
    // res.send({ msg: 'Hello This is a JSON' })
    
    // This should be prefered as it sends JSON
    // res.json('Hello this is also a JSON')

});

app.listen(5000, () => console.log('server started on 5000'));