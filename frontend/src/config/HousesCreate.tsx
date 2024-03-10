import React, { SyntheticEvent, useState } from 'react';
import Wrapper from './Wrapper';
import  {Navigate}  from 'react-router-dom';
import Nav from '../interfaces/Nav';

const HousesCreate = () => {
  const [name, setName] = useState('');
  const [image, setImage] = useState('');
  const [description, setDescription] = useState('');
  const [redirect, setRedirect] = useState(false);

  const submit = async (e: SyntheticEvent) => {
    e.preventDefault();

    await fetch('https://ed-4504743430324224.educative.run/api/houses', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        image,
        description,
      }),
    });

    setRedirect(true);
  };

  if (redirect) {
    return <Navigate to={'/config/houses'} />;
  }

  return (
    <Wrapper>
      <form onSubmit={submit}>
        <div className='form-group'>
          <label>Name</label>
          <input
            placeholder='Name'
            type='text'
            className='form-control'
            name='name'
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className='form-group'>
          <label>Image</label>
          <input
            placeholder='Image'
            type='text'
            className='form-control'
            name='image'
            onChange={(e) => setImage(e.target.value)}
          />
        </div>
        <div className='form-group'>
          <label>Description</label>
          <input
            placeholder='Description'
            type='text'
            className='form-control'
            name='description'
            onChange={(e) => setDescription(e.target.value)}
          />
        </div>
        <button className='btn btn-outline-secondary'>Save</button>
      </form>
    </Wrapper>
  );
};

export default HousesCreate;
