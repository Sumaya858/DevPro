import React, { useState } from 'react';
import axios from 'axios';

export default function Homepage() {
  const [name, setName] = useState('');
  const [image, setImage] = useState(null);
  const [owner] = useState(1); // Assuming default owner is 1
  const [description, setDescription] = useState('');
  const [previewImage, setPreviewImage] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === 'name') {
      setName(value);
    } else if (name === 'description') {
      setDescription(value);
    }
  };

  const handleImageChange = (e) => {
    const selectedImage = e.target.files[0];
    setImage(selectedImage);
    setPreviewImage(URL.createObjectURL(selectedImage));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('name', name);
    formData.append('image', image);
    formData.append('owner', owner);
    formData.append('description', description);

    axios
      .post('http://localhost:8000/api/items/', formData)
      .then((response) => {
        if (response.status === 200) {
          console.log('Item saved successfully.');
          // Reset the form or perform any necessary actions
        } else {
          console.error('Failed to save item.');
        }
      })
      .catch((error) => {
        console.error('Error occurred while saving item:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          type="text"
          name="name"
          value={name}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Image:
        <input type="file" name="image" onChange={handleImageChange} />
      </label>
      <br />
      {previewImage && (
        <img
          src={previewImage}
          alt="Selected"
          style={{ maxWidth: '200px', maxHeight: '200px' }}
        />
      )}
      <br />
      <label>
        Description:
        <input
          type="text"
          name="description"
          value={description}
          onChange={handleChange}
        />
      </label>
      <br />
      <button type="submit">Save</button>
    </form>
  );
}