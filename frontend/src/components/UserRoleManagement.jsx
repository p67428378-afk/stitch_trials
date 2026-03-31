import React from 'react';

const UserRoleManagement = () => {
  return (
    <section className='flex-shrink-0 w-80 space-y-8'>
      <div>
        <h2 className='font-headline text-2xl font-bold tracking-tight mb-2'>Workspace</h2>
        <p className='text-sm text-on-surface-variant font-medium'>Session Identity & Credentials</p>
      </div>
      <div className='bg-surface-container-low p-6 rounded-xl space-y-6'>
        <div className='bg-surface-container-lowest p-5 rounded-lg shadow-sm'>
          <div className='flex flex-col items-center text-center'>
            <div className='relative mb-4'>
              <div className='w-20 h-20 rounded-full border-2 border-primary-fixed overflow-hidden'>
                <img alt='Lead Dispatcher' data-alt='professional dispatcher avatar portrait in profile view' src='https://lh3.googleusercontent.com/aida-public/AB6AXuAiNcejvhFrwIphPH64a-ObZsuTwri3WB12DpMWl3WU1uYk8imF7gyONqcFffpiybFtZ-QCb-w4JNORIz0gSIrI8uvX4ZJ1bNOoz8C0y0ScEBfC55CyjiHUL3ClTYHGSn71BkABEFSdMXKq8NkrWYJegn2Bpfvq_avm2QxnRr6nrdfYMYMR7-rnmiywgNHb20nnKKYtB86I17pIEuAyVzT2V9EyJi5V7sk7RDhFgPPj0trKayKwZb7QKAWUW-lkMq2mPF7NJOHJvQxh'/>
              </div>
              <div className='absolute bottom-0 right-0 w-5 h-5 bg-tertiary-fixed rounded-full border-2 border-surface-container-lowest flex items-center justify-center'>
                <div className='w-2 h-2 bg-on-tertiary-container rounded-full'></div>
              </div>
            </div>
            <h3 className='font-headline font-bold text-lg'>Marcus Holloway</h3>
            <p className='text-xs font-semibold text-on-surface-variant mb-4 uppercase tracking-widest'>Lead Dispatcher</p>
            <div className='w-full space-y-2 text-left'>
              <p className='text-[10px] text-outline uppercase font-bold tracking-widest mb-1 px-1'>Switch Role</p>
              <button className='w-full flex items-center justify-between px-3 py-2 bg-surface-container text-sm font-medium rounded border border-outline-variant/30 hover:bg-surface-container-high transition-colors'>
                <span>Administrator</span>
                <span className='material-symbols-outlined text-sm'>unfold_more</span>
              </button>
              <button className='w-full flex items-center justify-between px-3 py-2 bg-surface-container text-sm font-medium rounded border border-outline-variant/30 hover:bg-surface-container-high transition-colors'>
                <span>Driver View</span>
                <span className='material-symbols-outlined text-sm'>unfold_more</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default UserRoleManagement;
