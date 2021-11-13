import React from 'react';
import './App.css';
import LandingPage from './LandingPage';
import Login from './Login';
import Schedule from './Schedule';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/" exact component={Home}/>
                    <Route path="/login" exact component={Login}/>
                    <Route path="/landingpage" exact component={LandingPage}/>
                    <Route path="/schedule" exact component={Schedule}/>
                </Switch>   
            </div>
        </Router>
    );
}

const Home = () => (
    <div>
        <h1>Home Page</h1>
    </div>
);

export default App;