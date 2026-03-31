import React from 'react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import UserRoleManagement from './components/UserRoleManagement';
import DispatchControl from './components/DispatchControl';
import RealtimeTracking from './components/RealtimeTracking';
import FinancialLedger from './components/FinancialLedger';
import OperationalAnalytics from './components/OperationalAnalytics';
import FloatingSummaryBar from './components/FloatingSummaryBar';

function App() {
  return (
    <div className='bg-surface font-body text-on-surface overflow-hidden'>
      <Navbar />
      <Sidebar />
      <main className='ml-72 pt-20 h-screen overflow-x-auto horizontal-canvas bg-surface scroll-smooth'>
        <div className='flex flex-row items-stretch h-full px-12 py-10 gap-24 min-w-[3200px]'>
          <UserRoleManagement />
          <DispatchControl />
          <RealtimeTracking />
          <FinancialLedger />
          <OperationalAnalytics />
        </div>
      </main>
      <FloatingSummaryBar />
    </div>
  );
}

export default App;
