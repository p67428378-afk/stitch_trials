import React from 'react';

function LiveOperationsMap() {
  return (
    <section className='flex-shrink-0 w-[1200px] space-y-8'>
      <div>
        <h2 className='font-headline text-2xl font-bold tracking-tight mb-2'>Global Live Operations</h2>
        <p className='text-sm text-on-surface-variant font-medium'>Real-time Telemetry &amp; Telematics</p>
      </div>
      <div className='flex gap-6 h-[550px]'>
        {/* Map Widget */}
        <div className='flex-1 bg-surface-container-low rounded-xl relative overflow-hidden'>
          <div className='absolute inset-0 grayscale contrast-125 opacity-40 mix-blend-multiply bg-cover bg-center' data-alt='minimalist city map schematic with clean vector lines and muted tones' data-location='London' style={{ backgroundImage: "url('https://lh3.googleusercontent.com/aida-public/AB6AXuBRycORSDfSGr_oYQpJAkSbET7ivVKUfIlJZK-mtz3MfhCTpRj_VhSPV3S_WmPft1yhqKVP3ipbj962nEyhnHeI-yDlrfthotIXUKoGyxF8AjjvEZAkBlwo1LswGb9GTHbyAAe9Ni_oIy5nNmEtBjz6SBQSeVGVyh1haUO6796jUon889fIv343ibr4HH-W6GB9X0cEtQKTL5OP1HMwIGbPeo246YDPdf29mi1tJxB0djo33-yVt9ynIlflPsVeCCpSPa2IKuUXuNKZ')" }}></div>
          {/* Marker Overlays (Simulated) */}
          <div className='absolute top-[20%] left-[30%] animate-pulse'>
            <span className='material-symbols-outlined text-on-tertiary-container bg-tertiary-fixed p-1 rounded-full shadow-lg' style={{ fontVariationSettings: "'FILL' 1" }}>local_taxi</span>
          </div>
          <div className='absolute top-[60%] left-[45%]'>
            <span className='material-symbols-outlined text-on-error-container bg-error-container p-1 rounded-full shadow-lg' style={{ fontVariationSettings: "'FILL' 1" }}>local_taxi</span>
          </div>
          <div className='absolute top-[40%] left-[75%]'>
            <span className='material-symbols-outlined text-on-tertiary-container bg-tertiary-fixed p-1 rounded-full shadow-lg' style={{ fontVariationSettings: "'FILL' 1" }}>local_taxi</span>
          </div>
          {/* Map HUD */}
          <div className='absolute top-6 left-6 bg-white/80 backdrop-blur-md p-4 rounded-lg shadow-sm space-y-4'>
            <div className='flex items-center gap-4'>
              <div>
                <p className='text-[10px] text-outline font-bold uppercase tracking-widest'>Active Units</p>
                <p className='text-xl font-headline font-extrabold'>2,482</p>
              </div>
              <div className='h-8 w-[1px] bg-outline-variant/30'></div>
              <div>
                <p className='text-[10px] text-outline font-bold uppercase tracking-widest'>Zone Alert</p>
                <p className='text-xl font-headline font-extrabold text-error'>High Traffic</p>
              </div>
            </div>
          </div>
          <div className='absolute bottom-6 right-6 flex gap-2'>
            <button className='bg-white p-2 rounded shadow-sm hover:bg-surface-container transition-colors'>
              <span className='material-symbols-outlined'>add</span>
            </button>
            <button className='bg-white p-2 rounded shadow-sm hover:bg-surface-container transition-colors'>
              <span className='material-symbols-outlined'>remove</span>
            </button>
            <button className='bg-primary text-on-primary p-2 rounded shadow-sm hover:opacity-90 transition-opacity'>
              <span className='material-symbols-outlined'>my_location</span>
            </button>
          </div>
        </div>
        {/* Ride Progress Sidebar */}
        <div className='w-80 bg-surface-container-low p-6 rounded-xl flex flex-col'>
          <h3 className='font-headline font-bold mb-6 flex items-center gap-2'>
            <span className='material-symbols-outlined text-on-tertiary-container'>speed</span>
            Ride Progress
          </h3>
          <div className='space-y-6 flex-1 overflow-y-auto pr-2'>
            <div className='space-y-2'>
              <div className='flex justify-between text-xs font-bold'>
                <span>TRIP-9021</span>
                <span className='text-on-tertiary-container'>ETA: 4 MIN</span>
              </div>
              <div className='h-1 w-full bg-outline-variant/20 rounded-full overflow-hidden'>
                <div className='h-full bg-on-tertiary-container w-[75%]'></div>
              </div>
              <p className='text-[10px] text-on-surface-variant font-medium'>In-progress: Marylebone to Soho</p>
            </div>
            <div className='space-y-2'>
              <div className='flex justify-between text-xs font-bold'>
                <span>TRIP-8843</span>
                <span className='text-on-tertiary-container'>ETA: 12 MIN</span>
              </div>
              <div className='h-1 w-full bg-outline-variant/20 rounded-full overflow-hidden'>
                <div className='h-full bg-on-tertiary-container w-[30%]'></div>
              </div>
              <p className='text-[10px] text-on-surface-variant font-medium'>In-progress: Heathrow to Victoria</p>
            </div>
            <div className='space-y-2'>
              <div className='flex justify-between text-xs font-bold'>
                <span>TRIP-9102</span>
                <span className='text-on-error-container'>DELAYED</span>
              </div>
              <div className='h-1 w-full bg-error-container rounded-full overflow-hidden'>
                <div className='h-full bg-error w-[90%]'></div>
              </div>
              <p className='text-[10px] text-on-surface-variant font-medium'>Alert: Heavy Traffic on M4</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default LiveOperationsMap;
