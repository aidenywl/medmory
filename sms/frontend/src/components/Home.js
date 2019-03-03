import React from "react";
import demo from "./Demo.mp4";

class Home extends React.Component {
  render() {
    return (
      <div>
        <video id="background-video" loop autoPlay style={styles.vidStyle}>
          <source src={demo} type="video/mp4" />
        </video>
      </div>
    );
  }
}

const styles = {
  vidStyle: {
    justifyContent: "center",
    alignItems: "center"
  }
};

export default Home;
