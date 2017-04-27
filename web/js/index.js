import React from 'react';
import ReactDOM from 'react-dom';
import Instruction from './components/Instruction.jsx';
import App from './components/App.jsx';

import { createStore } from 'redux';
import session from './reducers/session.js';

import request from 'ajax-request';

import { sampleQuestions } from './sampleQuestions.js';

// Initialize store
const store = createStore(session, {
	sessionState: 0,
	id: -1,
	questions: [],
	index: -1,
});

// Render the app.
const render = () => {
	const state = store.getState();
	const rootEl = document.getElementById('react-root');

	switch (state.sessionState) {
		case 0:
			// Get user ID and question list from backend.
			request({
			  url: 'http://localhost:5000/getSessionData',
			  json: true
			}, (err, res, body) => {
				// For testing purposes.
				if (err) {
					body = { id: 392, questions: sampleQuestions };
				}

				ReactDOM.render(
					<Instruction
						onClick={() => store.dispatch({ type: 'BEGIN_SESSION', data: body })}
						btnText="Begin"
						key={state.sessionState}
					>
						<p>Hello.</p>
	          <p>I would like to ask you a series of questions.</p>
	          <p>You may choose not to answer any of them.</p>
	          <p>In return, I will give you the responses of a previous participant. But only to the questions you also choose to answer.</p>
	          <p>When you are ready, click 'Begin'.</p>
					</Instruction>,
					rootEl
				);
			});
			break;

		case 1:
			ReactDOM.render(
				<App
					index = {state.index}
					question = {state.questions[state.index]}
					onSubmit = {(value) => store.dispatch({ type: 'SUBMIT', value: value })}
				/>,
				rootEl
			);
			break;

		case 2:
			ReactDOM.render(
				<Instruction
					onClick={() => store.dispatch({ type: 'FINISH_SESSION' })}
					btnText="Finish"
					key={state.sessionState}
				>
					<p>Thank you. Please remember to take your receipt.</p>
				</Instruction>,
				rootEl
			);
	}
}

render();
store.subscribe(render);
