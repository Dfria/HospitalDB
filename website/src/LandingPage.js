import React from 'react';
import './LandingPage.css';

function LandingPage() {
      return (
        <html>
            <head>
            </head>

            <body>
                <div id="header">
                    <h1 class="logo">Patient Info</h1>
                    <div id="menu">
                        <div class="elements">Setting</div>
                        <div class="elements">Stores</div>
                        <div class="elements">Payment</div>
                    </div>
                </div>

                <h2 id="title">Plan a visit</h2>

                <form>
                    <input id="zipcode-input" type="text" placeholder="Enter your zipcode" name="zipcode" required/>
                    <button for="zipcode-input" id="submit-button" type="submit" name="email">GET STARTED</button>
                </form>

                <div id="info">
                    <div class="photo">
                        <img class="icon" src="icon-solid-syringe-copy.PNG"/>
                    </div>
                    <div>
                        <h3>Covid 19 Vaccine</h3>
                        <p>Offers free COVID-19 vaccines, including boosters.</p>
                    </div>
                    <div class="photo">
                        <img class="icon" src="covid.png"/>
                    </div>
                    <div>
                        <h3>COVID-19 testing</h3>
                        <p>We are here to help you with COVID-19 testing. Many tests are available at no cost</p>
                    </div>
                    <div class="photo">
                        <img class="icon" src="lab-tube.png"/>
                    </div>
                    <div>
                        <h3>CODVID-19 antibody testing</h3>
                        <p>Antibody test reveal whether you are been infected with the virus that causes COVID-19 in the.</p>
                    </div>
                </div>

                <div id="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/BtN-goy9VOY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>

                <div id="options">
                    <div class="boxes">
                        <div class="option-names">Minor illnesses</div>
                        <h2>$60</h2>
                        <p>Strep.</p>
                        <p>Sore throat.</p>
                        <p>STDs.</p>
                        <p>Flu-like symptoms.</p>
                        <button type="button" class="select-button" src="#">SELECT</button>
                    </div>
                    <div class="boxes">
                        <div class="option-names">Minor injuries</div>
                        <h2>$90</h2>
                        <p>Bug bites.</p>
                        <p>Strings.</p>
                        <p>Sprains.</p>
                        <p>Joint pain.</p>
                        <button type="button" class="select-button" src="#">SELECT</button>
                    </div>
                    <div class="boxes">
                        <div class="option-names">Skin conditions</div>
                        <h2>$80</h2>
                        <p>Acne.</p>
                        <p>Chicken pox.</p>
                        <p>Shingles.</p>
                        <p>Lice.</p>
                        <button type="button" class="select-button" src="#">SELECT</button>
                    </div>
                </div>

                <div id="footer">
                    <div id="nav">
                        <p class="nav-1">Privacy</p>
                        <p class="nav-1">Terms</p>
                        <p class="nav-1">Contact</p>
                    </div>

                    <div id="nav-2">
                        Copyright 2016, Original Trombines
                    </div>


                </div>      
            </body>
        </html>
      )
    }
  
  export default LandingPage;