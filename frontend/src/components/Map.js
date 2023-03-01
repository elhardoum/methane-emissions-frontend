import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api";

function Wrap(props) {
  const API_KEY = process.env.REACT_APP_GOOGLE_API_KEY;

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: `${API_KEY}`,
  });
  if (!isLoaded) return <div> Loading ...</div>;

  return <Map {...props} />;
}

function Map(props) {
  const { lat=44, lng=-80 } = props

  return (
    <GoogleMap
      zoom={10}
      center={{ lat, lng }}
      mapContainerClassName="map-container"
    >
      <Marker position={{ lat, lng }} />
    </GoogleMap>
  );
}

export default Wrap;
