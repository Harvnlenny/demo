import * as React from 'react';
import { Component } from 'react';
import { BrowserRouter as Router, NavLink, Redirect, Route } from 'react-router-dom';
import './App.css';

import axios from 'axios';
import { Field, Form, Formik, FormikActions } from 'formik';

interface Values {
  email: string;
  password: string;
}

interface TodoProps {
  todo: string;
}

interface TodoState {
  isEditing?: boolean;
}

class App extends Component<any, any> {
  constructor(props: TodoProps) {
    super(props);
    this.state = {
      token: '',
    };
    this.handleClick = this.handleClick.bind(this);
  }
  public handleClick() {
    axios.post('http://www.mocky.io/v2/5c8119be3100003c24771d81').then(response => {
      const loginToken = response.data.token;
      console.log('loginToken', loginToken);
      this.setState({ token: response.data.token });
    });
  }
  public render() {
    return (
      <Router>
        <div className="App">
          <ul>
            <li>
              <NavLink to="/accounts/login" activeStyle={
                { color: 'red'}
              }>
                Login
              </NavLink>
            </li>
            <li>
              <NavLink to="/products" activeStyle={
                { color: 'red'}
              }>Products</NavLink>
            </li>
          </ul>

          <Route path="/accounts/login" exact render={
            () => {
              return ( 
                  <Formik
                    initialValues={{
                      email: '',
                      password: ''
                    }}
                    onSubmit={(values: Values, { setSubmitting }: FormikActions<Values>) => {
                      setTimeout(() => {
                        alert(JSON.stringify(values, null, 2));
                        setSubmitting(false);
                      }, 500);
                    }}
                    render={() => (
                      <Form>
                        <label htmlFor="email">Email</label>
                        <Field id="email" name="email" placeholder="email@example.com" type="text" />

                        <label htmlFor="password">Password</label>
                        <Field id="password" name="password" placeholder="password" type="text" />

                        <button type="submit" onClick={this.handleClick}>
                          Submit
                        </button>
                        <p>{this.state.token}</p>

                        <button type="reset">
                          Reset
                        </button>
                      </Form>
                    )}
                  />
                );
            }
          }
          />
          <Route path="/products" exact render={
            () => {
              return ( <h1>Products</h1>);
            }
          }
          />
        </div>
      </Router>
    );
  }
}

export default App;
