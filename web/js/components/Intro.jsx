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
        transitionEnter={true}
        transitionLeave={false}
        transitionAppearTimeout={500}
        transitionEnterTimeout={500}
      >
        <p className="text-center">Press any key to begin.</p>
      </CSSTransitionGroup>
    );
  }
}

Intro.propTypes = {
  onKeyPress: PropTypes.func.isRequired,
};

export default Intro;
