import { Schema, model } from 'mongoose'

const todoSchema = new Schema({
    completed: {
        type: Boolean,
        required: true
    },
    title: {
        type: String,
        required: true
    }
})

const Todo = model('Todo', todoSchema)

export default Todo;