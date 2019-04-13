import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import zxcvbn from 'zxcvbn'

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
        />
    )
}

class App extends React.Component {
    state = {
        password: "",
        time_online_throttled: "",
        time_online_no_throttling: "",
        time_offline_slow_hashing: "",
        time_offline_fast_hashing: "",
        warnings: "",
        suggestions: [],
    }

    onPassChange = (e) => {
        const password = e.target.value
        const evaluation = zxcvbn(password)
        console.log(evaluation)
        this.setState({
            password,
            score: evaluation.score,
            time_online_throttled: evaluation.crack_times_display.online_throttling_100_per_hour,
            time_online_no_throttling: evaluation.crack_times_display.online_no_throttling_10_per_second,
            time_offline_slow_hashing: evaluation.crack_times_display.offline_slow_hashing_1e4_per_second,
            time_offline_fast_hashing: evaluation.crack_times_display.offline_fast_hashing_1e10_per_second,
            warnings: evaluation.feedback.warning,
            suggestions: evaluation.feedback.suggestions,
        })
    }


    render() {
        const {score, time_online_throttled, time_online_no_throttling, time_offline_slow_hashing, time_offline_fast_hashing, warnings, suggestions} = this.state
        return (
            <div class='Container'>
                <div class='Page'>
                    <div class='OpeningHeader'>
                        <TypewriterComponent 
                            string1={header1} 
                            delay1='1500' 
                            string2={subheader1} 
                            delay2='1000' 
                            string3={subheader2}  
                        />
                    </div>
                    <div class='Continue'>
                        Scroll to continue...
                    </div>
                </div>
                <div class='Page'>
                    <div class='DictionaryCheck'>
                        <input
                            type='password'
                            value={this.state.password}
                            placeholder="password..."
                            onChange={this.onPassChange}
                        /> {score}
                        <ul>
                            <li>Online Throttled (100 guesses/hour): {time_online_throttled}</li>
                            <li>Online Unthrottled (10 guesses/second): {time_online_no_throttling}</li>
                            <li>Offline Strong Hashing (10 thousand guesses/second): {time_offline_slow_hashing}</li>
                            <li>Offline Weak Hashing (10 billion guesses/second): {time_offline_fast_hashing}</li>
                        </ul>
                        <ul>
                            <li>{warnings}</li>
                        </ul>
                        <ul>
                            {suggestions.map((s, index) =>
                                <li key={index}>{s}</li>
                            )}
                        </ul>
                    </div>
                </div>
            </div>
            );
    }
}

ReactDOM.render(
    <App />,
    document.getElementById('app')

)
