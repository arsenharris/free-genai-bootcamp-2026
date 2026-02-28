import React from 'react'
import { Link, useLocation } from 'react-router-dom'

function pretty(segment: string) {
  if (!segment) return 'Dashboard'
  return segment.replace('-', ' ').replace(/\b\w/g, (c) => c.toUpperCase())
}

export const Breadcrumbs: React.FC = () => {
  const loc = useLocation()
  const parts = loc.pathname.split('/').filter(Boolean)

  return (
    <div className="flex items-center gap-2 text-sm">
      <Link to="/dashboard" className="text-slate-600">Dashboard</Link>
      {parts.map((p, i) => {
        const to = '/' + parts.slice(0, i + 1).join('/')
        return (
          <React.Fragment key={to}>
            <span className="text-slate-400">&gt;</span>
            <Link to={to} className="text-slate-700">
              {pretty(p)}
            </Link>
          </React.Fragment>
        )
      })}
    </div>
  )
}
