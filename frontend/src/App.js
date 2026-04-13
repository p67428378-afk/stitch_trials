import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import LiveMap from './components/LiveMap';
import UserManagement from './components/UserManagement';
import Reports from './components/Reports';
import Payments from './components/Payments';
import CabOperations from './components/CabOperations';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-gray-800 p-4 text-white">
          <ul className="flex space-x-4">
            <li>
              <Link to="/live-map">Live Map</Link>
            </li>
            <li>
              <Link to="/user-management">User Management</Link>
            </li>
            <li>
              <Link to="/reports">Reports</Link>
            </li>
            <li>
              <Link to="/payments">Payments</Link>
            </li>
            <li>
              <Link to="/cab-operations">Cab Operations</Link>
            </li>
          </ul>
        </nav>

        <div className="container mx-auto mt-4">
          <Routes>
            <Route path="/live-map" element={<LiveMap />} />
            <Route path="/user-management" element={<UserManagement />} />
            <Route path="/reports" element={<Reports />} />
            <Route path="/payments" element={<Payments />} />
            <Route path="/cab-operations" element={<CabOperations />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

function Home() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Welcome to the Cab Management System</h1>
      <p>Please select a section from the navigation above.</p>
    </div>
  );
}

export default App;
