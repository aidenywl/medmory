import React, { Component } from "react";
import { Image, Menu, Segment } from "semantic-ui-react";
import logo from "./logo.png";

export default class Menubar extends Component {
  state = { activeItem: "home" };

  handleItemClick = (e, { name }) => {
    this.setState({ activeItem: name });
    this.props.handler(name);
  };

  render() {
    const { activeItem } = this.state;

    return (
      <Segment inverted>
        <Menu inverted pointing secondary>
          <Image src={logo} size="tiny" style={styles.logo} />
          <Menu.Item
            name="home"
            active={activeItem === "home"}
            onClick={this.handleItemClick}
          />
          <Menu.Item
            name="demo"
            active={activeItem === "demo"}
            onClick={this.handleItemClick}
            style={{ float: "right" }}
          />
        </Menu>
      </Segment>
    );
  }
}

const styles = {
  logo: {
    width: 100,
    height: 100,
    margin: 5,
    resizeMode: "contain"
  }
};
