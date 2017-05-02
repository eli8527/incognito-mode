import request from 'ajax-request'

export default (state, action) => {
	switch (action.type) {

		case 'BEGIN':
			return {...state, sessionState: 0}

		case 'BEGIN_SESSION':
			return {
				...state,
				sessionState: 1,
				id: action.data.id,
				questions: action.data.questions,
				index: 0
			};

		case 'FINISH_SESSION':
			request.post({
				url: 'http://localhost:5000/finish',
				json: true,
				data: {
					id: state.id,
				}
			}, (err, res, body) => {
				if (err) {
					console.log(err);
				}
			});
			return {...state, sessionState: -1};

		case 'SUBMIT':
			if (isValidAnswer(action.value)) {
				request.post({
					url: 'http://localhost:5000/submit',
					json: true,
					data: {
						id: state.id,
						qid: state.questions[state.index].qid,
						answer: action.value,
					}
				}, (err, res, body) => {
					if (err) {
						console.log(err);
					}
				});
			}

			if (state.index < state.questions.length - 1) {
				return {...state, index: state.index + 1};
			} else {
				return {...state, sessionState: 2};
			}

		default:
			return state;
	}
}

function isValidAnswer(value) {
	return !!value.trim();
}
