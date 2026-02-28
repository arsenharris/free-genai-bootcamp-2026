import React from 'react'
import { NavLink } from 'react-router-dom'

const links = [
  { to: '/dashboard', label: 'Dashboard' },
  { to: '/study-activities', label: 'Study Activities' },
  { to: '/words', label: 'Words' },
  { to: '/groups', label: 'Word Groups' },
  { to: '/session', label: 'Sessions' },
  { to: '/settings', label: 'Settings' }
]

export const NavBar: React.FC = () => {
  return (
    <header className="neobrutal p-4 flex items-center justify-between">
      <div className="flex items-center gap-4">
        <div className="text-xl font-bold">Spanish Portal</div>
      </div>
      <nav className="flex gap-3">
        {links.map((l) => (
          <NavLink
            key={l.to}
            to={l.to}
            className={({ isActive }) =>
              `px-3 py-1 rounded-sm ${isActive ? 'bg-darkBorder text-white' : ''}`
            }
          >
            {l.label}
          </NavLink>
        ))}
      </nav>
    </header>
  )
}
