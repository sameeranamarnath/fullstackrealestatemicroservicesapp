import React from 'react';
import './App.css';
import { BrowserRouter, Route } from 'react-router-dom';
import HousesUpdate from './config/HousesUpdate';
import HousesCreate from './config/HousesCreate';
import Houses from './config/Houses';

function App() {
  return (
    <div className='App'>
      <BrowserRouter>
        <Route path='/config/houses/:id/update'  Component={HousesUpdate} />
        <Route path='/config/houses/:id/create'  Component={HousesCreate} />
        <Route path='/config/houses/'  Component={Houses} />
        
        
      </BrowserRouter>
    </div>
  );
}

export default App;
