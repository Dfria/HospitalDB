import React, {Component} from 'react';
import './Schedule.css';

function Schedule() {
    return (
        <div>
            <body>
                <h1 id="title">Make an Appoinment</h1>
                <p id="description">Thank you for choosing us</p>
                <div>
                    <form id="appointment-form">
                        <label id="name-label">Name</label>
                        <br/>
                        <input id="name" class="input" type="text" placeholder="Enter your name" required/>
                        <br/>
                        <label id="email-label">Email</label>
                        <input id="email" class="input" type="email" placeholder="Enter your Email" required/>
                        <label id="number-label" for="number">Age <span class="smaller">(optional)</span></label>
                        <input id="number" class="input" type="number" placeholder="Age" pattern="0-9" min="1" max="150"
                        required/>
                        <label for="roles">Choose available physician</label>
                        <select name="current-role" id="dropdown">
                            <option value="" selected disabled >Select physicians</option>
                            <option value="john">John</option>
                            <option value="christ">Christ</option>
                            <option value="jose">Jose</option>
                            <option value="helen">Helen</option>
                            <option value="max">Max</option>
                        </select>  
                        <label>What is level of emergency</label>
                        <br/>
        
                        <div id="smaller">
                            <label for="radio-recommendation"> <input type="radio" id="radio-recommendation" name="recommendation" value="Definitely"/>
                                Urgent
                            </label>
        
                            <br/>
        
                            <label for="radio-recommendation"> <input type="radio" id="radio-recommendation" name="recommendation" value="Maybe"/>
                                Not urgent
                            </label>
        
                            <br/>
        
                            <label for="radio-recommendation"> <input type="radio" id="radio-recommendation" name="recommendation" value="Not-sure"/>
                                Not sure
                            </label>
                        </div>
        
                        <label>When do you want to make an appoinment</label>
        
                        <select name="current-role" id="dropdown">
                            <option value="" selected disabled >Select an option</option>
                            <option value="challenges">8-9am</option>
                            <option value="projects">10-11am</option>
                            <option value="community">1-2pm</option>
                            <option value="opensource">3-4pm</option>
                            <option value="free">5-6pm</option>
                        </select>  
        
                        <label>What is your health situation? <span class="smaller">(Check all that apply)</span></label>
        
                        <div id="smaller">
                            <label for="minor-injuries"><input value="minor-injuries" name="improved" type="checkbox"/>Minor injuries</label><br/>
                            <label for="sleep-disorders"><input value="sleepdisorders" name="improved" type="checkbox"/>Sleep disorders</label><br/>
                            <label for="high-blood-pressure"><input value="high-blood-pressure" name="improved" type="checkbox"/>High blood pressure</label><br/>
                            <label for="high-cholesterol"><input value="high-cholesterol" name="improved" type="checkbox"/>High cholesterol</label><br/>
                            <label for="mental-health-counseling"><input value="mental-health-counseling" name="improved" type="checkbox"/>Mental health counseling</label><br/>
                            
                        </div>
        
                        <label>Any comments or notes?</label>
                        <textarea id="input-comment" type="text" placeholder="Enter your comment here..."></textarea>
                        <div id="submit-botton"><input type="submit" id="submit" value="submit"/></div>
                    </form>
                </div>
                
                
            </body>
        </div>
    )
}

export default Schedule;
