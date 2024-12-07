import axios from 'axios'

//创建axios对象
const requst = axios.create({
    baseURL: 'http://localhost:8000/api', 
    timeout: 5000,
})



export default requst