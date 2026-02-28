import React from 'react'

export default function Settings(){
  return (
    <section>
      <h1 className="text-2xl font-semibold">Settings</h1>
      <div className="mt-4 neobrutal p-4">
        <div className="mb-4">
          <button className="neo-btn">Reset History</button>
        </div>
        <div>
          <label className="flex items-center gap-2">
            <input type="checkbox" /> Dark Mode
          </label>
        </div>
      </div>
    </section>
  )
}
