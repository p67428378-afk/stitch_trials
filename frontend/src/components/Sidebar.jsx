import React from 'react';

const Sidebar = () => {
  return (
    <aside className='fixed left-0 top-0 h-full flex flex-col p-4 z-40 bg-[#f2f4f6] text-slate-900 font-['Inter'] text-sm font-medium rounded-none h-screen w-72 no-border space-y-1 shadow-none pt-24'>
      <div className='mb-8 px-4 flex items-center gap-4'>
        <div className='w-12 h-12 rounded-lg bg-surface-container-highest overflow-hidden'>
          <img alt='User Profile' data-alt='close up headshot of lead dispatcher professional in workspace' src='https://lh3.googleusercontent.com/aida-public/AB6AXuDo8C3n_c7TlXY6CytvVcAx7uIVrG2Q3iuYZS0ePaq56vZZgSU4WJTFdcnIRc9qQI1jfor-inDSenRlWiqT7NvxswL7Tg-N1lw8HuzggTeJqNpagnmCSlFZ1Dz5Uw3CtT14g6TzONrCVcDcqqviG33qr12VCfYQ0EPZfYh1y_pGbXNFitP_aYcOsNHup04nFmjBjEeH3eNbwb_1P23C3SL2AyYxsO42QTw67lffofbVnviMyIYwgL2wAjAkRTZD-q9skPUXArbg7PLO'/>
        </div>
        <div>
          <p className='font-['Manrope'] font-bold text-slate-900 block leading-tight'>Lead Dispatcher</p>
          <p className='text-xs text-slate-500'>Admin Mode</p>
        </div>
      </div>
      <nav className='flex-1 space-y-1'>
        <div className='flex items-center gap-3 p-3 text-slate-500 hover:bg-slate-200/50 transition-all duration-200 ease-in-out cursor-pointer'>
          <span className='material-symbols-outlined' data-icon='pan_tool_alt'>pan_tool_alt</span>
          <span>Horizon View</span>
        </div>
        <div className='flex items-center gap-3 p-3 bg-white text-slate-950 rounded-md shadow-sm font-bold transition-all duration-200 ease-in-out cursor-pointer'>
          <span className='material-symbols-outlined' data-icon='local_taxi'>local_taxi</span>
          <span>Dispatch Hub</span>
        </div>
        <div className='flex items-center gap-3 p-3 text-slate-500 hover:bg-slate-200/50 transition-all duration-200 ease-in-out cursor-pointer'>
          <span className='material-symbols-outlined' data-icon='explore'>explore</span>
          <span>Fleet Map</span>
        </div>
        <div className='flex items-center gap-3 p-3 text-slate-500 hover:bg-slate-200/50 transition-all duration-200 ease-in-out cursor-pointer'>
          <span className='material-symbols-outlined' data-icon='payments'>payments</span>
          <span>Revenue</span>
        </div>
        <div className='flex items-center gap-3 p-3 text-slate-500 hover:bg-slate-200/50 transition-all duration-200 ease-in-out cursor-pointer'>
          <span className='material-symbols-outlined' data-icon='database'>database</span>
          <span>System Logs</span>
        </div>
      </nav>
      <div className='p-4 text-[10px] uppercase tracking-widest text-slate-400'>V2.4.0</div>
    </aside>
  );
};

export default Sidebar;
