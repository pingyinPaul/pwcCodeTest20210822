import logo from './logo.svg';
import './App.css';
import React, { useCallback, useEffect, useState, useRef } from "react";
import { Alert, Button, Modal, ProgressBar } from "react-bootstrap";
import Board from 'react-trello'
import Avatar from 'react-avatar';
import HomeIcon from '@material-ui/icons/Home';
const Header = (props) => {

  console.log(props)
  return (
    <>
      <div className='row Header' >
        <div className='col-md-2 HeaderPortal'>
          <h3>
            Wishlist Portal</h3>
        </div>
        <div className='col-md-6'>
        </div>
        <div className='col-md-1 HeaderHome'>
          <HomeIcon />Home
        </div>
        <div className='col-md-1'>
          <Avatar name={props.userName} size='40px' round={true} />

        </div>
      </div>
    </>
  );
}

export default Header;
