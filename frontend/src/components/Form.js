import React, { useState } from "react";
import GoogleMap from "./Map";

// png
function Form() {
  const [selectedFile, setSelectedFile] = useState();
  const [isSelected, setIsSelected] = useState(false);
  const [lat, setLat] = useState();
  const [lng, setLng] = useState();
  const [pred, setPred] = useState();

  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
    setIsSelected(true);
  };

  const handleSubmission = () => {
    const formData = new FormData();

    formData.append("File", selectedFile);

    setLat(undefined);
    setLng(undefined);
    setPred(undefined);

    fetch("/api/post-image", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((result) => {
        const { lat, lng, dataset } = result;
        if (lat && lng) {
          setLat(+lat);
          setLng(+lng);
        }

        if (dataset && dataset[0]) {
          setPred(dataset[0]);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <div className="form">
      <h2>Upload a File</h2>

      {isSelected ? (
        <div>
          <p>Filename: {selectedFile.name}</p>
          <p>Filetype: {selectedFile.type}</p>
          <p>Size in bytes: {selectedFile.size}</p>
        </div>
      ) : (
        <p>Select a file to upload</p>
      )}
      <div className="form-bottom">
        <input type="file" name="file" onChange={changeHandler} />
        <button className="btn" onClick={handleSubmission}>
          Submit
        </button>
      </div>
      {!!pred && <pre>Prediction: {pred}</pre>}

      {Boolean(lat && lng) && <GoogleMap lat={lat} lng={lng} /> }
    </div>
  );
}

export default Form;
