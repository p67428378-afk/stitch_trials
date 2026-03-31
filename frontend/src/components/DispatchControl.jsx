import React from 'react';

const DispatchControl = () => {
  return (
    <section className='flex-shrink-0 w-[550px] space-y-8'>
      <div>
        <h2 className='font-headline text-2xl font-bold tracking-tight mb-2'>Dispatch Control</h2>
        <p className='text-sm text-on-surface-variant font-medium'>New Assignments & Queues</p>
      </div>
      <div className='grid grid-cols-1 gap-6'>
        {/* New Booking Form */}
        <div className='bg-surface-container-low p-6 rounded-xl'>
          <div className='flex items-center gap-2 mb-4'>
            <span className='material-symbols-outlined text-primary'>add_circle</span>
            <h3 className='font-headline font-bold'>New Booking</h3>
          </div>
          <form className='space-y-4'>
            <div className='grid grid-cols-2 gap-4'>
              <div className='space-y-1'>
                <label className='text-[10px] uppercase font-bold tracking-wider text-outline'>Pickup Point</label>
                <input className='w-full bg-surface-container-lowest border-none text-sm p-3 rounded-sm focus:ring-1 focus:ring-primary' placeholder='Central Station' type='text'/>
              </div>
              <div className='space-y-1'>
                <label className='text-[10px] uppercase font-bold tracking-wider text-outline'>Drop-off</label>
                <input className='w-full bg-surface-container-lowest border-none text-sm p-3 rounded-sm focus:ring-1 focus:ring-primary' placeholder='LHR Airport T5' type='text'/>
              </div>
            </div>
            <div className='grid grid-cols-2 gap-4'>
              <div className='space-y-1'>
                <label className='text-[10px] uppercase font-bold tracking-wider text-outline'>Passenger</label>
                <input className='w-full bg-surface-container-lowest border-none text-sm p-3 rounded-sm focus:ring-1 focus:ring-primary' placeholder='John Doe' type='text'/>
              </div>
              <div className='space-y-1'>
                <label className='text-[10px] uppercase font-bold tracking-wider text-outline'>Vehicle Class</label>
                <select className='w-full bg-surface-container-lowest border-none text-sm p-3 rounded-sm focus:ring-1 focus:ring-primary'>
                  <option>Premium Sedan</option>
                  <option>MPV 7-Seater</option>
                  <option>Electric Eco</option>
                </select>
              </div>
            </div>
            <button className='w-full bg-primary text-on-primary py-3 font-bold text-xs uppercase tracking-widest rounded-sm hover:opacity-90 transition-opacity'>Confirm Booking</button>
          </form>
        </div>
        {/* Pending Dispatches */}
        <div className='bg-surface-container-low p-6 rounded-xl flex-1 overflow-hidden flex flex-col'>
          <div className='flex items-center justify-between mb-4'>
            <div className='flex items-center gap-2'>
              <span className='material-symbols-outlined text-primary'>pending_actions</span>
              <h3 className='font-headline font-bold'>Pending Dispatches</h3>
            </div>
            <span className='bg-primary text-on-primary text-[10px] font-bold px-2 py-1 rounded-full'>48 Active</span>
          </div>
          <div className='space-y-3'>
            <div className='bg-surface-container-lowest p-4 rounded-lg flex items-center justify-between'>
              <div>
                <p className='text-sm font-bold'>Booking #4402 - Sarah J.</p>
                <p className='text-xs text-on-surface-variant'>King's Cross → Canary Wharf</p>
              </div>
              <button className='bg-secondary-container text-on-secondary-container px-4 py-2 text-xs font-bold rounded-sm'>Assign Driver</button>
            </div>
            <div className='bg-surface-container-lowest p-4 rounded-lg flex items-center justify-between'>
              <div>
                <p className='text-sm font-bold'>Booking #4405 - Robert M.</p>
                <p className='text-xs text-on-surface-variant'>Paddington → Westminster</p>
              </div>
              <button className='bg-secondary-container text-on-secondary-container px-4 py-2 text-xs font-bold rounded-sm'>Assign Driver</button>
            </div>
            <div className='bg-surface-container-lowest p-4 rounded-lg flex items-center justify-between'>
              <div>
                <p className='text-sm font-bold'>Booking #4409 - Elena V.</p>
                <p className='text-xs text-on-surface-variant'>Waterloo → South Kensington</p>
              </div>
              <button className='bg-secondary-container text-on-secondary-container px-4 py-2 text-xs font-bold rounded-sm'>Assign Driver</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default DispatchControl;
