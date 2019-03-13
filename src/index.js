import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import Typewriter from 'typewriter-effect';

const header1 = 'Your passwords aren\'t as secure as you think they are.'
// const header2 = 'as you think they are.'
const subheader1 = ' However,'
const subheader2 = ' we can fix that.'

function TypewriterComponent (props) {
    return (
        <Typewriter
            options={{
                delay: 60,
            }}
            onInit={(typewriter) => {
                typewriter
                    .pauseFor(1000)
                    .typeString(props.string1)
                    .pauseFor(props.delay1)
                    .typeString(props.string2)
                    .pauseFor(props.delay2)
                    .typeString(props.string3)
                    .start();
            }}
            onFin={(typewriter) => {
                typewriter.stop();
            }}
        />
    )
}



function App () {
    return (
        <div>
            <div class='OpeningHeader'>
                <TypewriterComponent 
                    string1={header1} 
                    delay1='2000' 
                    string2={subheader1} 
                    delay2='1000' 
                    string3={subheader2}  
                />
            </div>
           
        </div>
        )
    }

ReactDOM.render(
    <App />,
    document.getElementById('app')

)
