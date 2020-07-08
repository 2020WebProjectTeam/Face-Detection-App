import React, { Component } from "react";
import { Link } from "react-router-dom";
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { logout } from '../../actions/auth';

export class Header extends Component {


  static propTypes = {
    auth: PropTypes.object.isRequired,
    logout: PropTypes.func.isRequired
  };

  render() {
    const { isAuthenticated, user } = this.props.auth;
    const authLinks = (
      <>
      <span className="navbar-text mr-3">
        <strong>{user ? `Welcome ${user.username}` : ""}</strong>
      </span>
      <div class="btn-group" role="group" aria-label="Basic example">
      <li className="nav-item">
        <a href="/app/upload/image/">
          <button className="nav-link btn btn-success text-light btn-sm"> Upload Image</button>
        </a>
      </li>
      <li className="nav-item">
        <button className="nav-link btn btn-info text-light btn-sm" onClick={this.props.logout}>Logout</button>
      </li>
      </div>
      </>
    );
    const guestLinks = (
      <>
      <li className="nav-item">
          <Link to="/register" className="nav-link">
          Register
          </Link>
      </li>
      <li className="nav-item">
          <Link to="/login" className="nav-link">
            Login
          </Link>
      </li>
      </>
    );
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <a className="navbar-brand" href="#">
          App
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
            { isAuthenticated ? authLinks : guestLinks }
          </ul>
        </div>
      </div>
      </nav>
    );
  }
}


const mapStateToProps = state => ({
  auth: state.auth,
});

export default connect(mapStateToProps, { logout })(Header);