import mongoose from "mongoose";

const MONGO_URL = "mongodb://dockermongo/testing"
// const MONGO_URL = "mongodb://oliver:oliver@localhost:27017/testing"

const connectDB = async () => {
    try {
        await mongoose.connect(MONGO_URL)
        console.log('db connected')
    } catch (error) {
        console.log(error)
        process.exit(1)
    }
}

export default connectDB