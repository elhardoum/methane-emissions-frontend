import React, { useState } from "react";

// png
function Form() {
  const [selectedFile, setSelectedFile] = useState();
  const [isSelected, setIsSelected] = useState(false);

  // let lat = 51.0447;
  // let lng = -114.0719;
  // let url = `https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyAlj0pxuucJSlRM71sIzoHXVQMqXk9C1Yo&markers=${lat},${lng}&size=640x640&zoom=11`;

  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
    setIsSelected(true);
  };

  const handleSubmission = () => {
    const formData = new FormData();

    formData.append("File", selectedFile);

    fetch("/api/post-image", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("Success:", result);
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

      <div>{/* <img className="map" src={url} alt="" /> */}</div>
    </div>
  );
}

export default Form;
