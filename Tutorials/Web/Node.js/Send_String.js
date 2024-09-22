const express = require('express');
const path = require('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) =>{

    // Sends Back the String
    res.send('Hello This is a String');
});

app.listen(5000, () => console.log('server started on 5000'));