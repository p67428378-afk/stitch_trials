import React from 'react';

function OperationalAnalytics() {
  return (
    <section className='flex-shrink-0 w-[800px] space-y-8 pr-12'>
      <div>
        <h2 className='font-headline text-2xl font-bold tracking-tight mb-2'>Operational Analytics</h2>
        <p className='text-sm text-on-surface-variant font-medium'>KPIs &amp; Performance Vectors</p>
      </div>
      <div className='grid grid-cols-3 gap-6'>
        <div className='bg-surface-container-low p-6 rounded-xl border-l-4 border-primary'>
          <p className='text-[10px] uppercase font-bold tracking-widest text-outline mb-2'>Total Rides</p>
          <p className='text-3xl font-headline font-extrabold'>1,240</p>
          <p className='text-[10px] text-on-tertiary-container font-bold mt-2'>↑ 12% vs LW</p>
        </div>
        <div className='bg-surface-container-low p-6 rounded-xl border-l-4 border-on-tertiary-container'>
          <p className='text-[10px] uppercase font-bold tracking-widest text-outline mb-2'>Active Drivers</p>
          <p className='text-3xl font-headline font-extrabold'>45</p>
          <p className='text-[10px] text-outline font-bold mt-2'>Peak Capacity</p>
        </div>
        <div className='bg-surface-container-low p-6 rounded-xl border-l-4 border-secondary'>
          <p className='text-[10px] uppercase font-bold tracking-widest text-outline mb-2'>Avg Wait Time</p>
          <p className='text-3xl font-headline font-extrabold'>4.2 min</p>
          <p className='text-[10px] text-on-error-container font-bold mt-2'>↓ 0.4m Improvement</p>
        </div>
      </div>
      <div className='bg-surface-container-low p-8 rounded-xl h-[350px] flex flex-col'>
        <div className='flex items-center justify-between mb-8'>
          <h3 className='font-headline font-bold'>Driver Performance Weekly</h3>
          <div className='flex gap-4'>
            <div className='flex items-center gap-2 text-[10px] font-bold'>
              <div className='w-3 h-3 bg-primary'></div>
              <span>COMPLETED</span>
            </div>
            <div className='flex items-center gap-2 text-[10px] font-bold'>
              <div className='w-3 h-3 bg-on-tertiary-container'></div>
              <span>RATING</span>
            </div>
          </div>
        </div>
        {/* Mock Bar Chart */}
        <div className='flex-1 flex items-end justify-between gap-4'>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-primary rounded-t-sm h-[80%]'></div>
            <span className='text-[10px] font-bold text-outline'>MON</span>
          </div>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-primary rounded-t-sm h-[65%]'></div>
            <span className='text-[10px] font-bold text-outline'>TUE</span>
          </div>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-primary rounded-t-sm h-[90%]'></div>
            <span className='text-[10px] font-bold text-outline'>WED</span>
          </div>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-primary rounded-t-sm h-[75%]'></div>
            <span className='text-[10px] font-bold text-outline'>THU</span>
          </div>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-primary rounded-t-sm h-[85%]'></div>
            <span className='text-[10px] font-bold text-outline'>FRI</span>
          </div>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-on-tertiary-container rounded-t-sm h-[40%]'></div>
            <span className='text-[10px] font-bold text-outline'>SAT</span>
          </div>
          <div className='flex flex-col items-center flex-1 gap-2'>
            <div className='w-full bg-on-tertiary-container rounded-t-sm h-[30%]'></div>
            <span className='text-[10px] font-bold text-outline'>SUN</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default OperationalAnalytics;
