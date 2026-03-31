import React from 'react';

const FinancialLedger = () => {
  return (
    <section className='flex-shrink-0 w-[600px] space-y-8'>
      <div>
        <h2 className='font-headline text-2xl font-bold tracking-tight mb-2'>Financial Ledger</h2>
        <p className='text-sm text-on-surface-variant font-medium'>Transactional Audit & Settlements</p>
      </div>
      <div className='space-y-6'>
        <div className='flex gap-4'>
          <div className='flex-1 bg-surface-container-low p-6 rounded-xl flex items-center justify-between'>
            <div>
              <p className='text-[10px] uppercase font-bold tracking-widest text-outline mb-1'>Total Revenue</p>
              <p className='text-2xl font-headline font-extrabold'>£142,500.00</p>
            </div>
            <span className='material-symbols-outlined text-3xl text-on-tertiary-container'>payments</span>
          </div>
          <button className='bg-primary text-on-primary px-8 rounded-xl font-bold text-xs uppercase tracking-widest hover:opacity-90 transition-all flex flex-col items-center justify-center gap-2'>
            <span className='material-symbols-outlined'>account_balance_wallet</span>
            Initiate Payment
          </button>
        </div>
        <div className='bg-surface-container-low p-6 rounded-xl overflow-hidden'>
          <div className='flex items-center justify-between mb-4'>
            <h3 className='font-headline font-bold'>Recent Transactions</h3>
            <span className='text-[10px] font-bold text-outline uppercase'>Last 24 Hours</span>
          </div>
          <table className='w-full text-xs'>
            <thead className='bg-surface-container-highest text-on-surface font-bold uppercase tracking-wider'>
              <tr>
                <th className='p-3 text-left'>ID</th>
                <th className='p-3 text-left'>Customer</th>
                <th className='p-3 text-left'>Amount</th>
                <th className='p-3 text-right'>Status</th>
              </tr>
            </thead>
            <tbody className='divide-y divide-outline-variant/10'>
              <tr className='bg-surface-container-lowest'>
                <td className='p-3 font-medium'>#TXN-8821</td>
                <td className='p-3'>Angela S.</td>
                <td className='p-3'>£42.50</td>
                <td className='p-3 text-right'>
                  <span className='bg-tertiary-fixed text-on-tertiary-container px-2 py-1 rounded-full text-[10px] font-bold'>PAID</span>
                </td>
              </tr>
              <tr className='bg-surface-container-low'>
                <td className='p-3 font-medium'>#TXN-8820</td>
                <td className='p-3'>Liam O.</td>
                <td className='p-3'>£18.00</td>
                <td className='p-3 text-right'>
                  <span className='bg-tertiary-fixed text-on-tertiary-container px-2 py-1 rounded-full text-[10px] font-bold'>PAID</span>
                </td>
              </tr>
              <tr className='bg-surface-container-lowest'>
                <td className='p-3 font-medium'>#TXN-8819</td>
                <td className='p-3'>TechCorp Ltd</td>
                <td className='p-3'>£312.45</td>
                <td className='p-3 text-right'>
                  <span className='bg-surface-container-highest text-outline px-2 py-1 rounded-full text-[10px] font-bold'>PENDING</span>
                </td>
              </tr>
              <tr className='bg-surface-container-low'>
                <td className='p-3 font-medium'>#TXN-8818</td>
                <td className='p-3'>Private Client</td>
                <td className='p-3'>£22.00</td>
                <td className='p-3 text-right'>
                  <span className='bg-error-container text-on-error-container px-2 py-1 rounded-full text-[10px] font-bold'>FAILED</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
};

export default FinancialLedger;
