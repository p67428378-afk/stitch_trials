import React from 'react';
import CabOperations from './components/CabOperations';
import UserManagement from './components/UserManagement';
import LiveMap from './components/LiveMap';
import Payments from './components/Payments';
import Reports from './components/Reports';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Welcome to the Cab Management System!
        </p>
      </header>
      <CabOperations />
      <UserManagement />
      <LiveMap />
      <Payments />
      <Reports />
    </div>
  );
}

export default App;
