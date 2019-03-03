import React, { Component } from "react";
import { Image, Menu, Segment } from "semantic-ui-react";

export default class Menubar extends Component {
  state = { activeItem: "home" };

  handleItemClick = (e, { name }) => this.setState({ activeItem: name });

  render() {
    const { activeItem } = this.state;

    return (
      <Segment inverted>
        <Menu inverted pointing secondary>
          <Image src={"./logo.png"} size="tiny" />
          <Menu.Item
            name="home"
            active={activeItem === "home"}
            onClick={this.handleItemClick}
          />
          <Menu.Item
            name="demo"
            active={activeItem === "friends"}
            onClick={this.handleItemClick}
            style={{ float: "right" }}
          />
        </Menu>
      </Segment>
    );
  }
}
