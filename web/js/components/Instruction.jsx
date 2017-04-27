import React from 'react';
import PropTypes from 'prop-types';
import CSSTransitionGroup from 'react-transition-group/CSSTransitionGroup';

import TypeWriter from 'react-typewriter';

class Instruction extends React.Component {

  constructor(props) {
    super(props);
    this.state = { showBtn: false };
  }

  render() {
    const delayMap = [
      { at: /\./, delay: 500 }
    ];

    const btn = this.state.showBtn ? (
      <CSSTransitionGroup
        transitionName="fade"
        transitionAppear={true}
        transitionEnter={true}
        transitionLeave={false}
        transitionAppearTimeout={500}
        transitionEnterTimeout={500}
      >
        <div className="button">
          <div onClick={this.props.onClick}>{this.props.btnText}</div>
        </div>
      </CSSTransitionGroup>
    ) : null;

    return (
      <div>
        <TypeWriter
          typing={1}
          maxDelay={50}
          delayMap={delayMap}
          onTypingEnd={() => setTimeout(() => this.setState({ showBtn:true }), 500)}
        >
          {this.props.children}
        </TypeWriter>

        { btn }
      </div>
    );
  }
}

Instruction.propTypes = {
  onClick: PropTypes.func.isRequired,
  btnText: PropTypes.string.isRequired,
};

export default Instruction;
