import React from 'react';
import './App.css';
import Home from './Home';
import Login from './Login';
import LandingPage from './LandingPage';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" exact component={<Home/>} />
                    <Route path="/login" component={Login} />
                    <Route path="/landingpage" component={LandingPage} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;