import React from 'react';
import './App.css';
import Login from './Login';
import LandingPage from './LandingPage';
import {BrowserRouter, useRoutes, Routes, Route} from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Routes>
                    <Route path="/" component={Home}/>
                    <Route path="/login" component={Login}/>
                </Routes>
                
            </div>
        </BrowserRouter>
    );
}

const Home = () => (
    <div>
        <h1>Home Page</h1>
    </div>
);

export default App;