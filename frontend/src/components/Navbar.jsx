import React from 'react';

function Navbar() {
  return (
    <nav className='bg-[#f7f9fb]/80 backdrop-blur-xl text-slate-900 font-["Manrope"] font-semibold tracking-tight docked full-width top-0 z-50 shadow-none flex items-center justify-between px-8 w-full h-20'>
      <div className='flex items-center gap-8'>
        <span className='text-xl font-black text-slate-950 tracking-tighter'>Fleet Control Center</span>
        <div className='hidden md:flex items-center gap-6'>
          <a className='text-slate-500 hover:bg-slate-100 transition-colors px-3 py-1 cursor-pointer active:opacity-70' href='#'>Horizon View</a>
          <a className='text-slate-950 border-b-2 border-slate-900 px-3 py-1 cursor-pointer active:opacity-70' href='#'>Dispatch Hub</a>
          <a className='text-slate-500 hover:bg-slate-100 transition-colors px-3 py-1 cursor-pointer active:opacity-70' href='#'>Fleet Map</a>
          <a className='text-slate-500 hover:bg-slate-100 transition-colors px-3 py-1 cursor-pointer active:opacity-70' href='#'>Revenue</a>
        </div>
      </div>
      <div className='flex items-center gap-4'>
        <div className='w-10 h-10 rounded-full bg-surface-container overflow-hidden'>
          <img alt='Dispatcher Profile' data-alt='professional portrait of a middle-aged male dispatcher wearing a headset in a modern command center' src='https://lh3.googleusercontent.com/aida-public/AB6AXuDxNOw_YkQ0f0wO7tueXDHgq9wv7hOo0ilCMm2hBiZ8TEYXp5Vh3owzR0pLR3p2p6katjPY9Big5guXPBwEFKR5vPe28j7HnGpyvXbE7BxNDe8Qw9Ze7OSIVLMUD4K3Q4X6btb8BJyNVyXl4pvTmMJYboKblxpaWhylcob90a8ZHU9FGuzRtGImdFF_C-HkoozP7SUfIwFjg4wp5K9uBv3-nOgxRclJWyX_18SyCimbpgVrt-qU8JQMP8LuWw0s1nlQr6pFG-bw7wL2'/>
        </div>
        <span className='material-symbols-outlined text-slate-900 cursor-pointer'>tune</span>
      </div>
    </nav>
  );
}

export default Navbar;
