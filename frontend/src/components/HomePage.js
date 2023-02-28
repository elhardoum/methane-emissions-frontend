import { GoogleMap, useLoadScript, Marker } from "@react-google-maps/api";

function HomePage() {
  const API_KEY = process.env.REACT_APP_GOOGLE_API_KEY;

  const { isLoaded } = useLoadScript({
    googleMapsApiKey: `${API_KEY}`,
  });
  if (!isLoaded) return <div> Loading ...</div>;

  return <Map />;
}

function Map() {
  return (
    <GoogleMap
      zoom={10}
      center={{ lat: 44, lng: -80 }}
      mapContainerClassName="map-container"
    >
      <Marker position={{ lat: 44, lng: -80 }} />
    </GoogleMap>
  );
}

export default HomePage;
