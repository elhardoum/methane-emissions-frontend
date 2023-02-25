import React from "react";
import GoogleMapReact from "google-map-react";
import Location from "./Location";

function HomePage() {
  const defaultProps = {
    center: {
      lat: 10.99835602,
      lng: 77.01502627,
    },
    zoom: 11,
  };

  return (
    <div style={{ height: "100vh", width: "100%" }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: "AIzaSyAlj0pxuucJSlRM71sIzoHXVQMqXk9C1Yo" }}
        defaultCenter={defaultProps.center}
        defaultZoom={defaultProps.zoom}
      >
        <Location lat={59.955413} lng={-30.337844} text="My Marker" />
      </GoogleMapReact>
    </div>
  );
}

export default HomePage;
