import React from 'react';
import '../css/Testimony.css'
function Testimony(props){
  return(
    <div className='testimony-container'>
      <img 
        className='image-testimony' 
        src={require(`../img/testimony-${props.image}.png`)}
        alt='Foto de Emma'/>
      <div className='testimony-text-container'>
        <p className='testimony-name'>
          <strong>{props.name}</strong> in {props.country}
        </p>
        <p className='testimony-pos'>
          {props.position} at <strong>{props.business}</strong>
        </p>
        <p className='testimony-text'>
          "{props.testimony}"
        </p>
      </div>
    </div>
  );
}

export default Testimony;