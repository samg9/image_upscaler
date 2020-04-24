import React, { Component } from 'react';
import './App.css';
import FileDropper from './components/FileDropper/FileDropper.js';
import axios from 'axios';
import { MetroSpinner } from "react-spinners-kit";

const initialState = {
  selectedFile: null,
  loaded: 0,
  loading: false,
  img: null,
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
    this.setState({
      loading: true,
    });
    const data = new FormData()
    data.append('file', this.state.selectedFile)
    axios.post("http://localhost:5000/api/upload", data, { // receive two parameter endpoint url ,form data 
    }).then(res => { // then print response status
      this.setState({
        loading: false,
        img: res.data
      });
      console.log(this.state.img);
      console.log(res);
      console.log(res.statusText);
    })
  }

  render() {
    return (
      <div className="App">
        <FileDropper onChangeHandler={this.onChangeHandler} onClickHandler={this.onClickHandler} />
        <div id="inner">
          <MetroSpinner
            size={150}
            loading={this.state.loading}
          />
          <img src={this.state.img} alt="" />
        </div>

      </div>
    );
  }
}

export default App;
