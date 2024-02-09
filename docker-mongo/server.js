import express from 'express'
import morgan from 'morgan'
import todosRoutes from './todosRoutes.js'
import connectDB from './db.js'

const app = express();

app.use(express.json())
app.use(morgan('dev'))

app.use('/todos', todosRoutes)

const port = 5000;
app.listen(port, () => {
    connectDB().then(() => {
        console.log(`listening ${port}`)
    })
})
