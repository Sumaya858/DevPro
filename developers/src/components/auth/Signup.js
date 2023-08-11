import React, { useState } from 'react';

export default function Signup(props) {
  const [newUser, setNewUser] = useState({});

  const changeHandler = (e) => {
    const user = { ...newUser };
    user[e.target.name] = e.target.value;
    setNewUser(user);
  };

  const registerHandler = (e) => {
    e.preventDefault();
    props.register(newUser);
  };

  return (
    <form onSubmit={registerHandler}>
      <label>
        First Name:
        <input type="text" name="username" onChange={changeHandler} />
      </label>
      <br />
      <label>
        Email:
        <input type="email" name="address" onChange={changeHandler} />
      </label>
      <br />
    
      <label>
        Password:
        <input type="password" name="password1" onChange={changeHandler} />
      </label>
      <br />
      <label>
       Confirm Password:
        <input type="password" name="password2" onChange={changeHandler} />
      </label>
      <br />
      <button type="submit">Register</button>
    </form>
  );
}