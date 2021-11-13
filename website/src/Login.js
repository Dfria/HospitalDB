import React, {Component} from 'react';
import './Login.css';

class Login extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
          <div class="login">Login</div>
          <div>
              <form>
                  <div class="container">
                    <label for="userid">Account ID</label>
                    <br/>
                    <input type="text" name="userid" placeholder="Enter Account ID" required/>
                    <br/>

                    <label for="password">Password</label>
                    <br/>
                    <input type="password" name ="password" placeholder="Enter Password" required/>
                    <br/>

                    <button type="submit">Login</button>
                    <br/>
                    <label>
                      <input type="checkbox" name="remember"/>Remember me
                    </label>                    
                  </div>
                  
              </form>
          </div>
      </div>
    )
  }
}

export default Login;
