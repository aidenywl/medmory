import React from "react";
import Home from "./Home";
import RegistrationForm from "./RegistrationForm";
import Menubar from "./Menubar";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      view: "home"
    };
  }

  viewHandler = newView => {
    this.setState({ view: newView });
  };

  renderView = () => {
    if (this.state.view === "home") {
      return <Home />;
    } else {
      return <RegistrationForm />;
    }
  };

  render() {
    return (
      <div>
        <Menubar handler={this.viewHandler} />
        {this.renderView()}
      </div>
    );
  }
}

export default App;
