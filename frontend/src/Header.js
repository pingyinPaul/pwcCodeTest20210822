import logo from './logo.svg';
import './App.css';
import React, { useCallback, useEffect, useState, useRef } from "react";
import { Alert, Button, Modal, ProgressBar } from "react-bootstrap";
import Board from 'react-trello'
import Avatar from 'react-avatar';
import HomeIcon from '@material-ui/icons/Home';
function Header() {


  return (
    <>
      <div className='row Header' >
        <div className='col-md-2 HeaderPortal'>
          Wishlist Portal
        </div>
        <div className='col-md-6'>
        </div>
        <div className='col-md-1 HeaderHome'>
          <HomeIcon />Home
        </div>
        <div className='col-md-1'>
          <Avatar name="Admin" size='40px' round={true} />

        </div>
      </div>
    </>
  );
}

export default Header;
