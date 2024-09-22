const express = require('express');
const path = require('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {

    // Sends back the host info
    // res.send(req.header('host'))

    //Sends back the current user agent in use by the user
    // res.send(req.header('user-agent'))

    //sends back all the raw header data
    // res.send(req.rawHeaders)
});

app.listen(5000, () => console.log('Server Started on 5000'))