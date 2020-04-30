import React from 'react';
import './FileDropper.css';
const FileDropper = ({ onChangeHandler, onClickHandler }) => {

    return (
        <div className="container">
            <div className="row">
                <div className="offset-md-3 col-md-6">
                    <div className="form-group files">
                        <label><b>Upload Your File to be Upscaled</b></label>
                        <input type="file" className="form-control" multiple onChange={onChangeHandler} />
                    </div>
                    <div className="form-group">


                    </div>

                    <button type="button" className="btn btn-success btn-block" onClick={onClickHandler}>Upscale</button>

                </div>
            </div>
        </div>
    );


}
export default FileDropper;