import React from 'react';

function FloatingSummaryBar() {
  return (
    <div className='fixed bottom-6 left-80 right-12 bg-surface-container-lowest/80 backdrop-blur-md border border-outline-variant/20 h-16 rounded-xl shadow-lg flex items-center justify-between px-8 z-30'>
      <div className='flex items-center gap-12'>
        <div className='flex items-center gap-3'>
          <div className='w-2 h-2 rounded-full bg-on-tertiary-container'></div>
          <p className='text-xs font-bold uppercase tracking-wider'><span className='text-outline'>SYSTEM STATUS:</span> OPTIMAL</p>
        </div>
        <div className='flex items-center gap-3'>
          <span className='material-symbols-outlined text-outline text-sm'>schedule</span>
          <p className='text-xs font-bold uppercase tracking-wider'><span className='text-outline'>NEXT SYNC:</span> 45S</p>
        </div>
        <div className='flex items-center gap-3'>
          <span className='material-symbols-outlined text-outline text-sm'>hub</span>
          <p className='text-xs font-bold uppercase tracking-wider'><span className='text-outline'>REGION:</span> NORTH LONDON</p>
        </div>
      </div>
      <div className='flex items-center gap-6'>
        <button className='flex items-center gap-2 text-xs font-bold uppercase tracking-widest text-outline hover:text-on-surface transition-colors'>
          <span className='material-symbols-outlined text-lg'>download</span>
          Export Logs
        </button>
        <div className='h-6 w-[1px] bg-outline-variant/30'></div>
        <button className='bg-primary text-on-primary px-4 py-2 text-[10px] font-bold uppercase tracking-widest rounded-sm'>Quick Dispatch</button>
      </div>
    </div>
  );
}

export default FloatingSummaryBar;
