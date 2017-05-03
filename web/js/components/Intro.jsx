import React from 'react';
import PropTypes from 'prop-types';
import CSSTransitionGroup from 'react-transition-group/CSSTransitionGroup';

class Intro extends React.Component {

  componentDidMount() {
    const onKeyPress = this.props.onKeyPress;
    document.addEventListener('keydown', function begin(e) {
      document.removeEventListener('keydown', begin);
      onKeyPress();
    });
  }

  render() {
    return (
      <CSSTransitionGroup
        transitionName="fade"
        transitionAppear={true}
        transitionEnter={false}
        transitionLeave={true}
        transitionAppearTimeout={500}
        transitionLeaveTimeout={500}
      >
        <p className="text-center fade-in-out">Press any key to begin.</p>
      </CSSTransitionGroup>
    );
  }
}

Intro.propTypes = {
  onKeyPress: PropTypes.func.isRequired,
};

export default Intro;
