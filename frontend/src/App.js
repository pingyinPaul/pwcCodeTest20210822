import logo from './logo.svg';
import './App.css';
import React, { useCallback, useEffect, useState, useRef } from "react";
import { Alert, Button, Modal, ProgressBar } from "react-bootstrap";
import Board from 'react-trello'
import Header from './Header'
import DatePicker from "react-datepicker";
import moment from 'moment'
import '@devexpress/dx-react-grid-bootstrap4/dist/dx-react-grid-bootstrap4.css';
import Paper from '@material-ui/core/Paper';
import {
  GroupingState,
  IntegratedGrouping,
  SortingState,
  IntegratedSorting,
} from '@devexpress/dx-react-grid';
import {
  Grid,
  Table,
  TableHeaderRow,
  TableGroupRow,
  GroupingPanel,
  Toolbar,
} from '@devexpress/dx-react-grid-material-ui';
import ListIcon from '@material-ui/icons/List';
function App() {
  const [token, setToken] = useState()
  const [username, setUsername] = useState()
  const [password, setPassword] = useState()
  const [kanban, setKanban] = useState(true)
  const [statusList, setStatusList] = useState([])
  const [responseData, setReponseData] = useState([])
  const [data, setData] = useState();
  const [show, setShow] = useState(false);
  const [showUpdate, setShowUpdate] = useState(false);
  const [showCreate, setShowCreate] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const handleCloseCreate = () => setShowCreate(false);
  const handleShowCreate = () => setShowCreate(true);
  const handleCloseUpdate = () => setShowUpdate(false);
  const handleKanban = () => {
    if (kanban) { setKanban(false) }
    else { setKanban(true) }
  };

  const [dataTemp, setDataTemp] = useState({
    lanes: [
    ]
  });
  const [currentUser, setCurrentUser] = useState('admin');
  const REACT_APP_BACKEND_URL = 'http://127.0.0.1:8000'
  // New request 
  const [startDate, setStartDate] = useState(new Date());
  const [subject, setSubject] = useState()
  const [type, setType] = useState('Other')
  const [territory, setTerritory] = useState('Other')
  const [version, setVersion] = useState()
  const [assignee, setAssignee] = useState()
  const [description, setDescription] = useState()
  const [startDateUpdate, setStartDateUpdate] = useState(new Date());
  const [subjectUpdate, setSubjectUpdate] = useState()
  const [typeUpdate, setTypeUpdate] = useState()
  const [territoryUpdate, setTerritoryUpdate] = useState()
  const [versionUpdate, setVersionUpdate] = useState()
  const [assigneeUpdate, setAssigneeUpdate] = useState()
  const [descriptionUpdate, setDescriptionUpdate] = useState()
  const [currentCradId, setCurrentCardId] = useState()
  const [newColumn, setNewColumn] = useState()
  const [columns, setColumns] = useState([
    { name: 'requestor', title: 'Requestor' },
    { name: 'description', title: 'Description' },
    { name: 'wish_type', title: 'Tag' },
    { name: 'date', title: 'Due date' },
    { name: 'updated_at', title: 'Last modified' },
    { name: 'status', title: 'Status' }
  ])
  const [rows, setRows] = useState([{
    "id": 4,
    "status": {
      "id": 1,
      "status": "Draft"
    },
    "date": "2021-08-21",
    "wish_type": "Other",
    "subject": "testing 1",
    "territory": "Other",
    "asignee": "Me",
    "version": "1",
    "description": "me agina",
    "updated_at": "2021-08-21T22:41:15.570812+08:00",
    "requestor": 118
  }])
  const handleShowUpdate = (cardId, metadata, laneId) => {
    setShowUpdate(true)
    const updateInstance = responseData.find(({ id }) => id === cardId);
    setStartDateUpdate(new Date(updateInstance.date))
    setSubjectUpdate(updateInstance.subject)
    setTypeUpdate(updateInstance.wish_type)
    setTerritoryUpdate(updateInstance.territory)
    setVersionUpdate(updateInstance.version)
    setAssigneeUpdate(updateInstance.asignee)
    setDescriptionUpdate(updateInstance.description)
    setCurrentCardId(cardId)
  };
  const login = async () => {
    const fetchRes = await fetch(
      `${REACT_APP_BACKEND_URL}/api/token/`,
      {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "username": username,
          "password": password
        })
      }
    );
    console.log(fetchRes.status)
    if (fetchRes.status === 500) {
      alert('Sever Error')
      return;
    }
    const res = await fetchRes.json();
    if (res.access) {
      console.log(res.access)
      setToken(res.access)
      loginHandler(res.access)
    }

  }
  const handleDrag = async (cardId, sourceLaneId, targetLaneId, position, cardDetails) => {
    console.log(cardId, sourceLaneId, targetLaneId, position, cardDetails)
    const content = {
      'status': targetLaneId,
    };
    const fetchRes = await fetch(
      `${REACT_APP_BACKEND_URL}/api/wishList/put/${cardId}/`,
      {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(content),
      }
    );
    if (fetchRes.status === 500) {
      alert('Sever Error')
      return;
    }
    var afterFetch = await fetching(token)
    console.log(afterFetch)
    setData(afterFetch)
  }
  let componentMounted = true; // (3) component is mounted

  async function getCardByReponse(responseStatus, response, i) {
    var thisCards = []
    console.log(response)
    for (let k = 0; k < response.length; k++) {
      console.log(response[k])
      console.log(k)
      if (response[k] == undefined) { continue }
      if (response[k].status == responseStatus[i]) {
        console.log('one of it', response[k].subject)
        var thisCardObj = {
          id: response[k].id,
          title: response[k].asignee,
          cardStyle: { "width": 270, "maxWidth": 270, "margin": "auto", "marginBottom": 5 },
          description: 'Subject: ' + response[k].subject + '\n' + 'Requestor: ' + response[k].requestor + '\n' + 'Tag: ' + response[k].wish_type + '\n' + 'Due Date: ' + response[k].date,
          label: 'Update:' + moment(response[k].date).format('YYYY-MM-DD')
        }
        thisCards.push(thisCardObj)
        console.log(thisCardObj)
      }
      else {
        continue;
      }
    }
    console.log('thisCard: ' + thisCards)
    return thisCards
  }

  async function fetching(tokenPass) {
    const resStatus = await fetch(
      `${REACT_APP_BACKEND_URL}/api/wishList/status/`,
      {
        method: "GET",
      }
    );
    if (resStatus.status === 500) {
      alert('Sever Error')
      return;
    }
    const responseStatus = await resStatus.json()
    console.log(responseStatus.status)
    await setStatusList(responseStatus.status)
    console.log(tokenPass)

    const res = await fetch(
      `${REACT_APP_BACKEND_URL}/api/wishList/`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${tokenPass}`,
        },
        // body: JSON.stringify({ user: 'admin' })
      }
    );
    if (res.status === 500) {
      alert('Sever Error')
      return;
    }
    const response = await res.json()
    console.log(response)
    var dataFromat = {
      lanes: [

      ],
      collapsibleLanes: true,
      cardDraggable: true,
      editable: true,
      canAddLanes: true,
      editLaneTitle: true
    }
    setReponseData(response)
    var showRes = response
    showRes.forEach(res => {
      res.status = res.status.status
      res.updated_at = moment(res.updated_at).format('YYYY-MM-DD')
    });
    setRows(showRes)
    for (var i = 0; i < responseStatus.status.length; i++) {
      console.log('hiohi')
      var thisCards = await getCardByReponse(responseStatus.status, response, i)
      var laneObj = {
        id: responseStatus.status[i],
        title: responseStatus.status[i],
        label: ' ',
        cards: thisCards
      }
      dataFromat['lanes'].push(laneObj)

    }
    console.log(response)
    return dataFromat
  }
  async function loginHandler(token) {

    var afterFetch = await fetching(token)
    console.log(afterFetch)
    setData(afterFetch)
  }

  function checkProperties(obj) {
    for (var key in obj) {
      if (obj[key] == null || obj[key] == "") {
        alert('Please input ' + key)
        return false;
      }
    }
    return true;
  }
  const handleSubmit = async () => {

    const content = {
      'requestor': currentUser,
      'subject': subject,
      'date': moment(startDate).format('YYYY-MM-DD'),
      'status': 'Draft',
      'wish_type': type,
      'territory': territory,
      'asignee': assignee,
      'version': version,
      'description': description
    };
    if (checkProperties(content)) {
      console.log(token)
      const fetchRes = await fetch(
        `${REACT_APP_BACKEND_URL}/api/wishList/post/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify(content),
        }
      );
      if (fetchRes.status === 500) {
        alert('Sever Error')
        return;
      }
      var afterFetch = await fetching(token)
      console.log(afterFetch)
      setData(afterFetch)
      handleClose()
    }
  }
  const handleSubmitUpdate = async () => {
    const content = {
      'subject': subjectUpdate,
      'date': moment(startDateUpdate).format('YYYY-MM-DD'),
      'wish_type': typeUpdate,
      'territory': territoryUpdate,
      'asignee': assigneeUpdate,
      'version': versionUpdate,
      'description': descriptionUpdate
    };
    if (checkProperties(content)) {
      const fetchRes = await fetch(
        `${REACT_APP_BACKEND_URL}/api/wishList/put/${currentCradId}/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify(content),
        }
      );
      if (fetchRes.status === 500) {
        alert('Sever Error')
        return;
      }
      var afterFetch = await fetching(token)
      console.log(afterFetch)
      setData(afterFetch)
      handleCloseUpdate()
    }
  }
  const handleCreateStatus = async () => {
    const content = {
      'status': newColumn
    };
    if (checkProperties(content)) {
      const fetchRes = await fetch(
        `${REACT_APP_BACKEND_URL}/api/status/post/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
          body: JSON.stringify(content),
        }
      );
      if (fetchRes.status === 500) {
        alert('Sever Error')
        return;
      }
      const response = await fetchRes.json()
      console.log(response)
      var afterFetch = await fetching(token)
      console.log(afterFetch)
      setData(afterFetch)
      handleClose()
    }
  }
  const handleCardDelete = async (cardId, laneId) => {

    const fetchRes = await fetch(
      `${REACT_APP_BACKEND_URL}/api/wishList/put/${cardId}/`,
      {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    if (fetchRes.status === 500) {
      alert('Sever Error')
      return;
    }
    var afterFetch = await fetching(token)
    console.log(afterFetch)
    setData(afterFetch)

  }
  const thisStyles = {
    Draft: {
      backgroundColor: '#f5f5f5',
    },
    Submitted: {
      backgroundColor: '#FFF2E5',
    },
    Pending: {
      backgroundColor: '#F8EDED',
      borderBottom: 'solid',
      borderBottomWidth: ' 10px !important',
      borderBottomColor: 'red'
    },
    Completed: {
      backgroundColor: '#F8F7ED',
    },
    QA: {
      backgroundColor: '#F7F7ED',
    },
  };

  const TableRow = ({ row, ...restProps }) => (
    <Table.Row
      {...restProps}
      // eslint-disable-next-line no-alert
      // onClick={() => handleShowUpdate(JSON.stringify(row).id, 0, 0)}
      onClick={() => handleShowUpdate(row.id, 0, 0)}
      style={{
        cursor: 'pointer',
        ...thisStyles[row.status],
      }}
    />)
  return (
    <>
      <Modal show={show} onHide={handleClose} dialogClassName="modal-90w" size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header >
          <Modal.Title>New Request</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="modalInnerDiv">
            <label>
              Subject:
            </label>
            <input
              className="note"
              value={subject}
              placeholder=""
              onChange={(e) => setSubject(e.target.value)}
              required
            >
            </input>
          </div>
          <div className="modalInnerDiv">

            <label className='dueDate'>
              Due Date:
            </label>
            <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} className='note' />
          </div>
          <div className="modalInnerDiv">

            <label>
              Type:
            </label>
            <select value={type} className="note" onChange={(e) => setType(e.target.value)}>
              <option value="Wishlist"> Wishlist</option>
              <option value="Other"> Other</option>
            </select>

          </div>
          <div className="modalInnerDiv">

            <label>
              Territory:
            </label>
            <select value={territory} className="note" onChange={(e) => setTerritory(e.target.value)}>
              <option value="PwC Mekong"> PwC Mekong</option>
              <option value="Other"> Other</option>
            </select>


          </div>
          <div className="modalInnerDiv">

            <label>
              DM Version:
            </label>
            <input
              className="note"
              value={version}
              placeholder=""
              onChange={(e) => setVersion(e.target.value)}
              required
            >
            </input>
          </div>
          <div className="modalInnerDiv">

            <label>
              Assignee:
            </label>
            <input
              className="note"
              value={assignee}
              placeholder=""
              onChange={(e) => setAssignee(e.target.value)}
              required
            >
            </input>
          </div>
          <div className="modalInnerDiv">

            <label>
              Description:
            </label>
            <textarea
              className="note"
              value={description}
              placeholder="Request details"
              onChange={(e) => setDescription(e.target.value)}
              required
            >
            </textarea>
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSubmit}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
      <Modal show={showUpdate} onHide={handleCloseUpdate} dialogClassName="modal-90w" size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header >
          <Modal.Title>Ticket Information</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="modalInnerDiv">
            <label>
              Subject:
            </label>
            <input
              className="note"
              value={subjectUpdate}
              placeholder=""
              onChange={(e) => setSubjectUpdate(e.target.value)}
              required
            >
            </input>
          </div>
          <div className="modalInnerDiv">

            <label>
              Due Date:
            </label>
            <DatePicker selected={startDateUpdate} onChange={(date) => setStartDateUpdate(date)} className='note' />
          </div>
          <div className="modalInnerDiv">

            <label>
              Type:
            </label>
            <select value={typeUpdate} className="note" onChange={(e) => setTypeUpdate(e.target.value)}
            >
              <option value="Wishlist"> Wishlist</option>
              <option value="Other"> Other</option>
            </select>
          </div>
          <div className="modalInnerDiv">

            <label>
              Territory:
            </label>
            <select value={territoryUpdate} className="note" onChange={(e) => setTerritoryUpdate(e.target.value)}
            >
              <option value="PwC Mekong"> PwC Mekong</option>
              <option value="Other"> Other</option>
            </select>
          </div>
          <div className="modalInnerDiv">

            <label>
              DM Version:
            </label>
            <input
              className="note"
              value={versionUpdate}
              placeholder=""
              onChange={(e) => setVersionUpdate(e.target.value)}
              required
            >
            </input>
          </div>
          <div className="modalInnerDiv">

            <label>
              Assignee:
            </label>
            <input
              className="note"
              value={assigneeUpdate}
              placeholder=""
              onChange={(e) => setAssigneeUpdate(e.target.value)}
              required
            >
            </input>
          </div>
          <div className="modalInnerDiv">

            <label>
              Description:
            </label>
            <textarea
              className="note"
              value={descriptionUpdate}
              placeholder="Request details"
              onChange={(e) => setDescriptionUpdate(e.target.value)}
              required
            >
            </textarea>
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseUpdate}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSubmitUpdate}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
      <Modal show={showCreate} onHide={handleCloseCreate} dialogClassName="modal-90w" size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered>
        <Modal.Header >
          <Modal.Title>Add New Column</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="row">
            <label>
              New Column Name:
            </label>
            <input
              className="note"
              value={newColumn}
              placeholder=""
              onChange={(e) => setNewColumn(e.target.value)}
              required
            >
            </input>
          </div>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseCreate}>
            Close
          </Button>
          <Button variant="primary" onClick={handleCreateStatus}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>

      {token ? <div className="App">
        <Header />
        <div className='boardDiv'>
          <div className='row Boardheader'>

            <div className='col-md-4 requestHeader'> All request</div>
            <div className='col-md-4 '> </div>
            <div className='col-md-1 requestHeader' > {kanban ?
              <Button onClick={handleKanban} size='sm' variant="light"> <ListIcon />List View </Button>
              : <Button onClick={handleKanban} size='sm' variant="light"> Board view</Button>}
            </div>
            <div className='col-md-2 newRequest'> <Button onClick={handleShow} size='sm' variant="light"> New request</Button>  <Button onClick={handleShowCreate} size='sm' variant="light"> New Column</Button></div>

          </div>
        </div>
        <div className='boardDiv'>
          {kanban ? <Board data={data ? data : dataTemp} handleDragEnd={handleDrag} onCardClick={handleShowUpdate} onCardDelete={handleCardDelete} style={{ width: '95vw', height: '80vh', backgroundColor: 'white' }} />
            : <Paper>
              <Grid
                rows={rows}
                columns={columns}
              >
                <SortingState
                  defaultSorting={[{ columnName: 'date', direction: 'asc' }]}
                />
                <GroupingState
                  grouping={[{ columnName: 'status' }]}
                />
                <IntegratedSorting />

                <IntegratedGrouping />

                <Table rowComponent={TableRow} />
                <TableHeaderRow showSortingControls />
                <TableGroupRow />
                <Toolbar />
                <GroupingPanel showSortingControls />
              </Grid>
            </Paper>}
        </div>
      </div> :
        <div className="App">
          <div className="row">
            <label>Username</label><input placeholder='admin1 / requestor1/ requestor2' value={username} onChange={(e) => setUsername(e.target.value)}
            ></input>
          </div>
          <div className='row'>
            <label>Password</label><input placeholder='admin234567 / re234567/ re234567' value={password} onChange={(e) => setPassword(e.target.value)}
            ></input>
          </div>
          <button onClick={login}>Login </button>
        </div>
      }
    </>

  );
}

export default App;
