
import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'https://insurance-the-api-of-risks.herokuapp.com/api/'
})
