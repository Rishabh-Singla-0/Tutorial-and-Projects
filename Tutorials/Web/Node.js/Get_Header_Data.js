const express = request('express');
const path = request('path');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.post('/contact', (req, res) => {
    res.send(req.body)
});

app.listen(5000, () => console.log('Server Started on 5000'))