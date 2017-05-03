import React from 'react';
import PropTypes from 'prop-types';
import CSSTransitionGroup from 'react-transition-group/CSSTransitionGroup';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = { value: '' };
    this.handleChange = this.handleChange.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.handleKeyPress = this.handleKeyPress.bind(this);
  }

  handleChange(e) {
    this.setState({value: e.target.value});
  }

  handleClick(e) {
    this.setState({ value: '' });
    this.props.onSubmit(this.state.value);
  }

  handleKeyPress(e) {
    if (e.key === 'Enter') {
      this.setState({ value: '' });
      this.props.onSubmit(this.state.value);
    }
  }

  renderInput(question) {
    switch (question.qtype) {
      case 'short':
        return (
          <input
            autoFocus
            spellCheck={false}
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
            onKeyPress={this.handleKeyPress} />
        );
      case 'long':
        return (
          <textarea
            autoFocus
            spellCheck={false}
            rows="5"
            value={this.state.value}
            onChange={this.handleChange}
            onKeyPress={this.handleKeyPress} />
        );
    }
  }

  render() {
    const question = this.props.question;

    return (
      <div>
        <CSSTransitionGroup
          transitionName="fade"
          transitionAppear={true}
          transitionEnter={true}
          transitionLeave={false}
          transitionAppearTimeout={500}
          transitionEnterTimeout={500}
        >
          <div key={question.qid}>
            <h1>{question.qtext}</h1>

            { this.renderInput(question) }

            <div id="previous-answers">
              Previously answered {question.qcount} times.
            </div>
          </div>
        </CSSTransitionGroup>

        <div className="button">
          <div className="submit" onClick={this.handleClick}>&rarr;</div>
        </div>
      </div>
    );
  }
}

App.propTypes = {
  index: PropTypes.number.isRequired,
  question: PropTypes.object.isRequired,
  onSubmit: PropTypes.func.isRequired,
};

export default App;
