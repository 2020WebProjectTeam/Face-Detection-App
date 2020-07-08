import React, { Fragment, useState } from 'react';
// import axios from 'axios';

// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

// var csrftoken = getCookie('csrftoken');

// const CSRFToken = () => {
//     return (
//         <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
//     );
// };

const FileUpload = () => {
    // let file, filename;
    const [file, setFile] = useState('');
    const [filename, setFilename] = useState('Choose File');
    const [uploadedFile, setUploadedFile] = useState({});
  
    const onChange = e => {
    //   file = e.target.files[0];
    //   filename = e.target.files[0].name;
      setFile(e.target.files[0]);
      setFilename(e.target.files[0].name);
    };
  
    const onSubmit = e => {
    //   e.preventDefault();
    //   const formData = new FormData();
    //   formData.append('file', file);
    //   console.log(formData);
      console.log(file);



      // try {
      //   const res = await axios.post('/api/images/', formData, {
      //     headers: {
      //       'Content-Type': 'multipart/form-data'
      //     }
      //   });
      //   console.log(res);
      //   const { fileName, filePath } = res.data;
      //   setUploadedFile({ fileName, filePath });
  
      // } catch (err) {
      //   // if (err.response.status === 500) {
      //   //   setMessage('There was a problem with the server');
      //   // } else {
      //   //   setMessage(err.response.data.msg);
      //   // }
      // }
    };
  
    return (
      <Fragment>
        <form method="post" action="/app/upload/image/" encType="multipart/form-data">
        {/* <CSRFToken /> */}
          <div className='custom-file mb-4'>
            <input
              type='file'
              className='custom-file-input'
              id='customFile'
              onChange={onChange}
              name="image"
            />
            <label className='custom-file-label' htmlFor='customFile'>
              {filename}
            </label>
          </div>  
          <input
            type='submit'
            value='Upload'
            className='btn btn-primary btn-block mt-4'
          />
        </form>
      </Fragment>
    );
  };
  
  export default FileUpload;