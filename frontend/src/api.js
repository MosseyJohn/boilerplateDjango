// Import axios for making HTTP requests
import axios from 'axios';
// Import ACCESS_TOKEN constant from our constants file
import { ACCESS_TOKEN } from './constants';

const apiUrl = '/choreo-apis/djangoreactboilerplate/backend/v1';

// Create an axios instance with a base URL
// The base URL is taken from the environment variable VITE_API_URL
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,
});

// Add a request interceptor
// This will run before every request made using this api instance
// It retrieves the access token from local storage and adds it to the request headers if it exists
// If there's an error in the request configuration, it rejects the promise with the error
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// The 'api' constant can now be used throughout the application
// to make authenticated requests to our backend

export default api;
