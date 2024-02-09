import { Router } from 'express'
import Todo from './Todo.js'

const router = Router()

router.get('/', async (req, res) =>{
    const todos = await Todo.find()
    res.json({todos})
});
router.post('/', async (req, res) =>{
    const {completed, title} = req.body
    const todo = await Todo.create({completed, title})
    res.json({todo})
});
router.get('/:id', async (req, res) =>{
    const {id} = req.params
    const todo = await Todo.findById(id)
    res.json({todo})
});
router.put('/:id', async (req, res) =>{
    const {id} = req.params
    const {completed, title} = req.body
    const updateTodo = {}
    if(completed) updateTodo.completed = completed
    if(title) updateTodo.title = title
    const todo = await Todo.findByIdAndUpdate(id, updateTodo, {new: true})
    res.json({todo})
});
router.delete('/:id', async (req, res) =>{
    const {id} = req.params
    const todo = await Todo.findById(id)
    await todo.delete()
    res.json({todo})
});
export default router;