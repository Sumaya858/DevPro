import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom'
import axios from 'axios'
import {useEffect, useState} from 'react'
import React from 'react'
// import { useNavigate } from 'react-router-dom';

// Import Components.
import Signin from './components/auth/Signin'
// import Signout from './components/auth/Signout'
import Signup from './components/auth/Signup'
import Homepage from './components/homepage/Homepage'


// Import Css
import './CSS/homepage.css'

export default function App() {
  
  const [isAuth, setIsAuth] = useState(false); 
  const [user, setUser] = useState({}); 
  
  useEffect(() => {
    let token = localStorage.getItem("token")
    if (token != null) {
      // let user = jwt_decode(token)
      let user = token
      setIsAuth(true)
      setUser(user)
    } 
    else if (!user) {
      localStorage.remove("token")
      setIsAuth(false)
    }

  },[user])

  

  


  const registerHandler = (user) => {
    console.log('here is register handler')
    axios.post("http://127.0.0.1:8000/auth/register/", user)
    .then(res => {
      console.log(res)
    }) 
    .catch(err => {
      console.log(err)
    })
    window.location.pathname= '/signin';
  }
  
  const loginHandler = (credential) => {
    console.log('login')
    axios.post("/auth/login/", credential)
    .then(res => {
     
      console.log(res.data.key)
     
      let token = res.data.key
      if (token != null) {
        localStorage.setItem("token", token)
        let user = token
        setIsAuth(true)
        setUser(user)
      }
    })
    .catch(err => {
      console.log(err)
    })
  }

  const logoutHandler = (e) => {
    e.preventDefault() //do not reload the page
    localStorage.removeItem("token");
    setIsAuth(false)
    setUser(null);
    window.location.pathname= '/homepage'; // Redirect to the homepage

  }

  
  return (
    <>
    <Router>

    <div className='navbar'>
      <ul>
        {isAuth?
        
      <>
       Welcome, 
       
       <li><Link to="/logout" onClick={logoutHandler}><strong>Logout</strong></Link> </li>

      </>
      :

      
      <li>
          
      <Link to="/signup"><strong>Signup</strong></Link> &nbsp;
      <Link to="/signin"><strong>Signin</strong></Link>&nbsp;&nbsp;
      <Link to="/homepage"><strong>Homepage</strong></Link>&nbsp;&nbsp;
     
    </li>
      }

       
      </ul>
      {/* //element={isAuth ? <Navigate to='/homepage' />}  */}






      <Routes>
      <Route path="/homepage" element={<Homepage />}></Route>
       <Route path="/signup" element={<Signup register={registerHandler}></Signup>}></Route>
       <Route path="/signin" element={isAuth ? <Navigate to='/homepage' /> : <Signin login={loginHandler}></Signin>}></Route>
       

         
      </Routes>
      



    </div>
    </Router>



    </>
  )
}
