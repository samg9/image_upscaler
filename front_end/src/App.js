import React, { Component } from 'react';
import './App.css';
import FileDropper from './components/FileDropper/FileDropper.js';
import axios from 'axios';

const initialState = {
  selectedFile: null,
  loaded: 0,
  isLoading: false,
}

class App extends Component {
  constructor() {
    super();
    this.state = initialState;
  }

  onChangeHandler = event => {
    this.setState({
      selectedFile: event.target.files[0],
      loaded: 0,
    })
  }
  onClickHandler = () => {
    const data = new FormData()
    data.append('file', this.state.selectedFile)
    axios.post("http://localhost:5000/api/upload", data, { // receive two parameter endpoint url ,form data 
    }).then(res => { // then print response status
      this.setState({
        isLoading: false,
      });
      console.log(res.statusText)
    })
  }

  render() {
    return (
      <div className="App">
        <FileDropper onChangeHandler={this.onChangeHandler} onClickHandler={this.onClickHandler} />
      </div>
    );
  }
}

export default App;
