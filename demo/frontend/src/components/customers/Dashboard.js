import React, { Fragment } from 'react';
import Form from './Form';
import Customers from './Customer';
import FileUploader from "../common/FileUpload";

function Dashboard() {
    return (
        <Fragment>
            {/* <h4 className="display-4 text-center mb-4">Image Upload</h4>
            <div className="card card-body mt-4 mb-4">
            <FileUploader /> */}
            {/* </div> */}
            <Form />
            <Customers />
        </Fragment>
    )
}

export default Dashboard